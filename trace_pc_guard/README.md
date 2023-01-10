### 1.查看当前符号顺序 Build Settings -> Write Link Map File -> Yes
	1.clean
	2.build
	3.Products -> show in finder
	4. Intermediates.noindex -> xxx.build -> Debug-iphonesimulator -> xxx.build -> xxx-LinkMap-normal-x86_64
	5. _# Symbols:_ 部分  对比Build Phases -> Compile Sources部分

### 2.读取编译顺序 Build Settings -> Other C Flags 

`-fsanitize-coverage=func,trace-pc-guard`
`代码见TestViewController.m`

### 3.设置插桩后order文件 Build Settings -> Order File 
`${SRCROOT}/lb.order`

