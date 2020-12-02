
## 检查项目中未使用的方法

##  python FindSelectorsUnrefs.py -a /Users/a58/Library/Developer/Xcode/DerivedData/XXX-bqqoxganvkvgwuefbskxsbvnxlnn/Build/Products/Debug-iphonesimulator/XXX.app -p /Users/a58/Desktop/ProjectPath -w WB,JD


## 参数说明：
-a Xcode运行之后的，项目Product路径
-p 项目的地址
-w 结果白名单处理，检测结果，只想要以什么开头的类的方法，多个用逗号隔开，比如JD,BD,AL
-b 结果黑名单处理,检测结果，不想要以什么开头的类的方法，多个用逗号隔开,比如Pod,AF,SD
-w 和 -b 不能共存，共存会报错


