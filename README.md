## appIcon
    批量生产iPhone、iPad需要的各尺寸icon图
    
## launchImage
    批量生产iPhone、iPad需要的各尺寸launchImage图
    
## assetContents
    批量修改Assets.xcassets里文件名称。执行环境 Python3
    
## classNames
    批量修改工程里文件名称。执行环境 Python3

## archive 自动打包
    自动打store包，上传到商店
    自动打hoc包，上传蒲公英
    
## tool_framework 
    动态库Debug Release合并脚本 
    1.File->New->Target->Aggregate
    2.Build Phases->Target Dependencies->+->SDK
    3.+->Add Run Script->...
    
## selectorUnrefs 
    查找未使用的方法 

## imageUnrefs 
    查找未使用的图片 
    
## xcode_tool
    OC控制台打印输出汉字
    
## xcode10_libstdc
    xcode10增加libstdc++文件类
    
## Pods-xx-frameworks.sh: /bin/sh: bad interpreter: Operation not premitted
    stackoverflow: https://stackoverflow.com/questions/38497708/when-i-built-my-app-in-xcode-there-is-an-error-bin-sh-bad-interpreter-operati
    Reason: If you download project from internet, executable .sh files will be quarantined, and system doesn't allow them to execute.
    Cure: You should remove extended attributes to make these executables work.
    In terminal
    xattr -rc 报错目录

## 备注
    终端执行脚本./*sh文件如有报错-bash: ./launchImage.sh: Permission denied
    1.可执行chmod u+x *.sh，这里的u这里指文件所有者，+x 添加可执行权限，*.sh表示所有的sh文件
    2.chmod 777 xx.sh，指令ls -al可查看当前目录下文件权限-rw-r--r--，
    第一个跟参数跟chmod无关,先不管，2-4参数:属于user，5-7参数:属于group，
    8-10参数:属于others，接下来就简单了:r==>可读 w==>可写 x==>可执行，
    r=4，w=2，x=1。所以755代表 rwxr-xr-x，代表用户对该文件拥有读，写，执行的权限，
    同组其他人员拥有执行和读的权限，没有写的权限，其他用户的权限和同组人员权限一样。
    777代表，user,group ,others ,都有读写和可执行权限。
