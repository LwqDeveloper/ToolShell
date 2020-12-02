# coding:utf-8

import os
import re
import sys
import getopt

reserved_prefixs = ["-[", "+["]


# 获取入参参数
def input_parameter():
    opts, args = getopt.getopt(sys.argv[1:], '-a:-p:-w:-b:',
                               ['app_path=', 'project_path=', 'black_list_Str', 'white_list_str'])

    black_list_str = ''
    white_list_str = ''
    white_list = []
    black_list = []
    # 入参判断
    for opt_name, opt_value in opts:
        if opt_name in ('-a', '--app_path'):
            # .app文件路径
            app_path = opt_value
        if opt_name in ('-p', '--project_path'):
            # 项目文件路径
            project_path = opt_value
        if opt_name in ('-b', '--black_list_Str'):
            # 检测黑名单前缀，不检测谁
            black_list_Str = opt_value
        if opt_name in ('-w', '--white_list_str'):
            # 检测白名单前缀，只检测谁
            white_list_str = opt_value

    if len(black_list_str) > 0:
        black_list = black_list_str.split(",")

    if len(white_list_str) > 0:
        white_list = white_list_str.split(",")

    if len(white_list) > 0 and len(black_list) > 0:
        print("\033[0;31;40m白名单【-w】和黑名单【-b】不能同时存在\033[0m")
        exit(1)

    # 判断文件路径存不存在
    if not os.path.exists(project_path):
        print("\033[0;31;40m输入的项目文件路径【-p】不存在\033[0m")
        exit(1)

    app_path = verified_app_path(app_path)
    if not app_path:
        exit('输入的app路径不存在，停止运行')

    return app_path, project_path, black_list, white_list


def verified_app_path(path):
    if path.endswith('.app'):
        appname = path.split('/')[-1].split('.')[0]
        path = os.path.join(path, appname)
        if appname.endswith('-iPad'):
            path = path.replace(appname, appname[:-5])
    if not os.path.isfile(path):
        return None
    if not os.popen('file -b ' + path).read().startswith('Mach-O'):
        return None
    return path


# 获取protocol中所有的方法
def header_protocol_selectors(file_path):
    # 删除路径前后的空格
    file_path = file_path.strip()
    if not os.path.isfile(file_path):
        return None
    protocol_sels = set()
    file = open(file_path, 'r')
    is_protocol_area = False
    # 开始遍历文件内容
    for line in file.readlines():
        # 删除注释信息
        # delete description
        line = re.sub('\".*\"', '', line)
        # delete annotation
        line = re.sub('//.*', '', line)
        # 检测是否是 @protocol
        # match @protocol
        if re.compile('\s*@protocol\s*\w+').findall(line):
            is_protocol_area = True
        # match @end
        if re.compile('\s*@end').findall(line):
            is_protocol_area = False
        # match sel
        if is_protocol_area and re.compile('\s*[-|+]\s*\(').findall(line):
            sel_content_match_result = None
            # - (CGPoint)convertPoint:(CGPoint)point toCoordinateSpace:(id <UICoordinateSpace>)coordinateSpace
            if ':' in line:
                # match sel with parameters
                # 【"convertPoint:"，"toCoordinateSpace:"]
                sel_content_match_result = re.compile('\w+\s*:').findall(line)
            else:
                # - (void)invalidate;
                # match sel without parameters
                # invalidate;
                sel_content_match_result = re.compile('\w+\s*;').findall(line)

            if sel_content_match_result:
                # 方法参数拼接
                # convertPoint:toCoordinateSpace:
                funcList = ''.join(sel_content_match_result).replace(';', '')
                protocol_sels.add(funcList)
    file.close()

    return protocol_sels


# 获取所有protocol定义的方法
def protocol_selectors(path, project_path):
    print('获取所有的protocol中的方法...')
    header_files = set()
    protocol_sels = set()
    # 获取当前引用的系统库中的方法列表
    system_base_dir = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk'
    # get system librareis
    lines = os.popen('otool -L ' + path).readlines()
    for line in lines:
        # 去除首尾空格
        line = line.strip()

        # /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer (compatibility version 1.0.0, current version 1.0.0)
        # /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
        # delete description,
        line = re.sub('\(.*\)', '', line).strip()

        if line.startswith('/System/Library/'):

            # [0:-1],获取数组的左起第一个，到倒数最后一个,不包含最后一个,[1,-1)左闭右开
            library_dir = system_base_dir + '/'.join(line.split('/')[0:-1])
            if os.path.isdir(library_dir):
                # 获取当前系统架构中所有的类
                # 获取合集
                header_files = header_files.union(os.popen('find %s -name \"*.h\"' % library_dir).readlines())

    if not os.path.isdir(project_path):
        exit('Error: project path error')
    # 获取当前路径下面所有的.h文件路径
    header_files = header_files.union(os.popen('find %s -name \"*.h\"' % project_path).readlines())

    for header_path in header_files:
        # 获取所有查找到的文件下面的protocol方法,这些方法，不能用来统计
        header_protocol_sels = header_protocol_selectors(header_path)
        if header_protocol_sels:
            protocol_sels = protocol_sels.union(header_protocol_sels)
    return protocol_sels


def imp_selectors(path):
    print('获取所有的方法，除了setter and getter方法...')
    # return struct: {'setupHeaderShadowView':['-[TTBaseViewController setupHeaderShadowView]']}
    #  imp     0x100001260 -[AppDelegate setWindow:] ==>> -[AppDelegate setWindow:],setWindow:
    re_sel_imp = re.compile('\s*imp\s*0x\w+ ([+|-]\[.+\s(.+)\])')
    re_properties_start = re.compile('\s*baseProperties 0x\w{9}')
    re_properties_end = re.compile('\w{16} 0x\w{9} _OBJC_CLASS_\$_(.+)')
    re_property = re.compile('\s*name\s*0x\w+ (.+)')
    imp_sels = {}
    is_properties_area = False

    # “otool - ov”将输出Objective - C类结构及其定义的方法。
    for line in os.popen('/usr/bin/otool -oV %s' % path).xreadlines():
        results = re_sel_imp.findall(line)
        if results:
            #  imp     0x100001260 -[AppDelegate setWindow:] ==>> [-[AppDelegate setWindow:],setWindow:]
            (class_sel, sel) = results[0]
            if sel in imp_sels:
                imp_sels[sel].add(class_sel)
            else:
                imp_sels[sel] = set([class_sel])
        else:
            # delete setter and getter methods as ivar assignment will not trigger them
            # 删除相关的set方法
            if re_properties_start.findall(line):
                is_properties_area = True
            if re_properties_end.findall(line):
                is_properties_area = False
            if is_properties_area:
                property_result = re_property.findall(line)
                if property_result:
                    property_name = property_result[0]
                    if property_name and property_name in imp_sels:
                        # properties layout in mach-o is after func imp
                        imp_sels.pop(property_name)
                        # 拼接set方法
                        setter = 'set' + property_name[0].upper() + property_name[1:] + ':'
                        # 干掉set方法
                        if setter in imp_sels:
                            imp_sels.pop(setter)
    return imp_sels


def ref_selectors(path):
    print('获取所有被调用的方法...')
    re_selrefs = re.compile('__TEXT:__objc_methname:(.+)')
    ref_sels = set()
    lines = os.popen('/usr/bin/otool -v -s __DATA __objc_selrefs %s' % path).readlines()
    for line in lines:
        results = re_selrefs.findall(line)
        if results:
            ref_sels.add(results[0])
    return ref_sels


def ignore_selectors(sel):
    if sel == '.cxx_destruct':
        return True
    if sel == 'load':
        return True
    return False


def filter_selectors(sels):
    filter_sels = set()
    for sel in sels:
        for prefix in reserved_prefixs:
            if sel.startswith(prefix):
                filter_sels.add(sel)
    return filter_sels


def unref_selectors(path, project_path):
    # 获取所有类的protocol的方法集合
    protocol_sels = protocol_selectors(path, project_path)

    # 获取项目所有的引用方法
    ref_sels = ref_selectors(path)
    if len(ref_sels) == 0:
        exit('获取项目所有的引用方法为空....')
    # 获取所有的方法，除了set方法
    imp_sels = imp_selectors(path)

    print("\n")
    if len(imp_sels) == 0:
        exit('Error: imp selectors count null')
    unref_sels = set()
    for sel in imp_sels:
        # 所有的方法，忽略白名单
        if ignore_selectors(sel):
            continue
        # 如果当前的方法不在protocol中，也不再引用的方法中，那么认为这个方法没有被用到
        # protocol sels will not apppear in selrefs section
        if sel not in ref_sels and sel not in protocol_sels:
            unref_sels = unref_sels.union(filter_selectors(imp_sels[sel]))
    return unref_sels


# 黑白名单过滤
def filtration_list(unref_sels, black_list, white_list):
    # 黑名单过滤
    temp_unref_sels = list(unref_sels)
    if len(black_list) > 0:
        # 如果黑名单存在，那么将在黑名单中的前缀都过滤掉
        for unref_sel in temp_unref_sels:
            for black_prefix in black_list:
                class_method = "+[%s" % black_prefix
                instance_method = "-[%s" % black_prefix
                if (unref_sel.startswith(class_method) or unref_sel.startswith(
                        instance_method)) and unref_sel in unref_sels:
                    unref_sels.remove(unref_sel)
                    break

    # 白名单过滤
    temp_array = []
    if len(white_list) > 0:
        # 如果白名单存在，只留下白名单中的部分
        for unref_sel in unref_sels:
            for white_prefix in white_list:
                class_method = "+[%s" % white_prefix
                instance_method = "-[%s" % white_prefix
                if unref_sel.startswith(class_method) or unref_sel.startswith(instance_method):
                    temp_array.append(unref_sel)
                    break
        unref_sels = temp_array

    return unref_sels


# 整理结果，写入文件
def write_to_file(unref_sels):
    file_name = 'selector_unrefs.txt'
    f = open(os.path.join(sys.path[0].strip(), file_name), 'w')
    unref_sels_num_str = '查找到未被使用的方法: %d个\n' % len(unref_sels)
    print(unref_sels_num_str)
    f.write(unref_sels_num_str)
    num = 1
    for unref_sel in unref_sels:
        unref_sels_str = '%d : %s' % (num, unref_sel)
        print(unref_sels_str)
        f.write(unref_sels_str + '\n')
        num = num + 1
    f.close()
    print('\n项目中未使用方法检测完毕，相关结果存储到当前目录 %s 中' % file_name)
    print('请在项目中进行二次确认后处理')


if __name__ == '__main__':
    # 获取入参
    app_path, project_path, black_list, white_list = input_parameter()

    # 获取未使用方法
    unref_sels = unref_selectors(app_path, project_path)

    # 黑白名单过滤
    unref_sels = filtration_list(unref_sels, black_list, white_list)

    # 打印写入文件
    write_to_file(unref_sels)
