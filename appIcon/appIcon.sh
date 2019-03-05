#!/bin/sh

imagepath_icon="./icon.png"

createiPhoneIconWithSize() {
sips -Z $1 ${imagepath_icon} --out ./AppIcon/icon_$1x$1.png
}

createiPadIconWithSize() {
sips -Z $1 ${imagepath_icon} --out ./AppIcon/iPad_$1x$1.png
}

createContentsOfJson(){
cat <<EOF >./AppIcon/Contents.json
{
"images" : [
{
"size" : "20x20",
"idiom" : "iphone",
"scale" : "2x",
"filename" : "icon_40x40.png"
},
{
"size" : "20x20",
"idiom" : "iphone",
"scale" : "3x",
"filename" : "icon_60x60.png"
},
{
"size" : "29x29",
"idiom" : "iphone",
"scale" : "2x",
"filename" : "icon_58x58.png"
},
{
"size" : "29x29",
"idiom" : "iphone",
"scale" : "3x",
"filename" : "icon_87x87.png"
},
{
"size" : "40x40",
"idiom" : "iphone",
"scale" : "2x",
"filename" : "icon_80x80.png"
},
{
"size" : "40x40",
"idiom" : "iphone",
"scale" : "3x",
"filename" : "icon_120x120.png"
},
{
"size" : "60x60",
"idiom" : "iphone",
"scale" : "2x",
"filename" : "icon_120x120.png"
},
{
"size" : "60x60",
"idiom" : "iphone",
"scale" : "3x",
"filename" : "icon_180x180.png"
},
{
"size" : "20x20",
"idiom" : "ipad",
"scale" : "1x",
"filename" : "iPad_20x20.png"
},
{
"size" : "20x20",
"idiom" : "ipad",
"scale" : "2x",
"filename" : "iPad_40x40.png"
},
{
"size" : "29x29",
"idiom" : "ipad",
"scale" : "1x",
"filename" : "iPad_29x29.png"
},
{
"size" : "29x29",
"idiom" : "ipad",
"scale" : "2x",
"filename" : "iPad_58x58.png"
},
{
"size" : "40x40",
"idiom" : "ipad",
"scale" : "1x",
"filename" : "iPad_40x40.png"
},
{
"size" : "40x40",
"idiom" : "ipad",
"scale" : "2x",
"filename" : "iPad_80x80.png"
},
{
"size" : "76x76",
"idiom" : "ipad",
"scale" : "1x",
"filename" : "iPad_76x76.png"
},
{
"size" : "76x76",
"idiom" : "ipad",
"scale" : "2x",
"filename" : "iPad_152x152.png"
},
{
"size" : "83.5x83.5",
"idiom" : "ipad",
"scale" : "2x",
"filename" : "iPad_167x167.png"
},
{
"size" : "1024x1024",
"idiom" : "ios-marketing",
"scale" : "1x",
"filename" : "icon_1024x1024.png"
}
],
"info" : {
"version" : 1,
"author" : "xcode"
}
}
EOF
}
# 1.清理旧目录
rm -rf AppIcon
# 2.生成新的空目录
mkdir AppIcon
# 3.生成Contents.json文件
createContentsOfJson
# 4.生成iPhone需要的icon
for iPhoneSize in  40 58 60 80 87 120 180 1024
    do
    createiPhoneIconWithSize $iPhoneSize
done
# 5.生成iPad需要的icon
for iPadSize in  20 29 40 58 76 80 152 167
    do
    createiPadIconWithSize $iPadSize
done

