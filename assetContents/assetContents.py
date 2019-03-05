import os

#文件前缀
filename_prefix = 'Youai'
#文件后缀
filename_suffix = 'MuStrong'

target_url = '/Users/01378859/work/company_Jiduo/Vest_Code/LoveOfPomelo/LoveOfPomelo/Assets.xcassets/Video'

def verify_filename(file_name):
    if file_name.endswith('.png') or file_name.endswith('.jpg'):
        return True
    return False

#遍历文件，符合规则的进行重命名
for (root, dirs, files) in os.walk(target_url):
    print('-----------')
    if len(files) == 2 :
        for file_name in files:
            if verify_filename(file_name):
                # 1.修改文件夹 xxx.imageset --> filename_prefix + 'xxx' + filename_suffix +'.imageset'
                file_path = os.path.join(root, file_name)
                fold_oldpath = file_path[:(len(file_path) - len(file_name) - 1)]
                fold_oldname = os.path.splitext(fold_oldpath.split('/')[-1])[0]
                fold_type = os.path.splitext(fold_oldpath.split('/')[-1])[1]
                fold_foldpath = fold_oldpath[0:len(fold_oldpath) - len(fold_oldname) - len(fold_type) - 1]
                fold_newname = filename_prefix + fold_oldname + filename_suffix
                fold_newpath = os.path.join(fold_foldpath, fold_newname + fold_type)
                os.renames(fold_oldpath, fold_newpath)
                print('fold_oldpath', fold_oldpath);
                print('fold_newpath', fold_newpath);
                
                # 2.修改 xxx.png --> filename_prefix + 'xxx' + filename_suffix +'.png'
                file_oldpath = file_path
                file_oldname = os.path.splitext(file_oldpath.split('/')[-1])[0]
                file_newname = fold_newname
                file_type = os.path.splitext(file_oldpath.split('/')[-1])[1]
                file_oldpath = fold_newpath + '/' + file_oldname + file_type
                file_newpath = fold_newpath + '/' + fold_newname + file_type
                os.renames(file_oldpath, file_newpath)
                print('file_oldpath', file_oldpath);
                print('file_newpath', file_newpath);
                
                # 3.修改Contents.json
                contents_path = fold_newpath + '/Contents.json'
                with open(contents_path, 'r+') as f2:
                    s = f2.read().replace(file_oldname, file_newname)
                    print(file_oldname + '--->' + file_newname)
                    f2.seek(0)
                    f2.write(s)
                    f2.truncate()
                    f2.close()


