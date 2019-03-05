import os

#文件前缀
filename_prefix = 'Youai'
#文件后缀
filename_suffix = 'Mustrong'

#需要更新文件目录
target_path = '/Users/01378859/demo/LoveOfPomelo/LoveOfPomelo'
#需要查询文件目录
project_path = '/Users/01378859/demo/LoveOfPomelo/LoveOfPomelo/Sections'
#工程文件地址
pbxpro_path = '/Users/01378859/demo/LoveOfPomelo/LoveOfPomelo.xcodeproj/project.pbxproj'

#文件重命名函数，返回新的文件名
def file_rename(file_path):
    print(file_path)
    root_path = os.path.split(file_path)[0]     # 文件目录
    root_name = os.path.split(file_path)[1]     # 文件名包含扩展名
    filename = os.path.splitext(root_name)[0]   # 文件名
    filetype = os.path.splitext(root_name)[1]   # 文件扩展名
    
    filename_new = filename
    if filename.startswith(filename_prefix) == False:
        filename_new = filename_prefix + filename_new
    if filename.encode(filename_suffix) == False:
        filename_new = filename_new + filename_suffix
    
    # 新文件名路径
    new_path = os.path.join(root_path, filename_new + filetype)    # 拼接新路径
    # 文件重命名
    os.renames(file_path, new_path)
    return filename_new

def verify_filename(file_name):
    if file_name.endswith('.h') or file_name.endswith('.m') or file_name.endswith('.mm'):
        return True
    return False

#定义一个字典 key=旧类名 value=新类名
needModifyDic = {}
needModifyFileNameDict = {}

#遍历文件，符合规则的进行重命名
for (root, dirs, files) in os.walk(project_path):
    for file_name in files:
        if verify_filename(file_name):
            old_name = os.path.splitext(file_name)[0]
            new_name = file_rename(os.path.join(root, file_name))
            needModifyDic[old_name] = new_name
            
            filetype = os.path.splitext(file_name)[1]  # 文件扩展名
            old_fileName = old_name + filetype
            new_fileName = new_name + filetype
            needModifyFileNameDict[old_fileName] = new_fileName

#遍历文件，在文件中更换新类名的引用
print('------------------------------')
for (root, dirs, files) in os.walk(target_path):
    for file_name in files:
        if verify_filename(file_name):
            print('-----folderName-------' + file_name)
            with open(os.path.join(root, file_name), 'r+') as f:
                s0 = f.read()
                f.close()
                for key in needModifyDic:
                    if key in s0:
                        with open(os.path.join(root, file_name), 'r+') as f4:
                            s1 = f4.read().replace(key, needModifyDic[key])
                            print(key + ' ------> ' + needModifyDic[key])
                            f4.seek(0)
                            f4.write(s1)
                            f4.truncate()
                            f4.close()
#替换配置文件中的类名
print('==============================')
for key in needModifyFileNameDict:
    with open(pbxpro_path, 'r+') as f:
        s0 = f.read()
        f.close()
        if key in s0:
            with open(pbxpro_path, 'r+') as f2:
                s = f2.read().replace(key, needModifyFileNameDict[key])
                print(key + ' ======> ' + needModifyFileNameDict[key])
                f2.seek(0)
                f2.write(s)
                f2.truncate()
                f2.close()
