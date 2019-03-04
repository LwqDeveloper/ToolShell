#---------------------------------配置工程信息---------------------------------
#archive类型 打包hoc 商店store
archive_type="store"
#工程名字(Target名字)
target_name="LoveOfPomelo"
#配置环境，Release或者Debug
configuration_type="Release"
#Bundle ID
target_bundleID="com.soft.youai"
#项目地址
project_path="/Users/01378859/work/company_Jiduo/Vest_Code/LoveOfPomelo"
 
#---------------------------------配置证书信息---------------------------------
#证书TeamID
cer_teamID="47WKTWKMY6"
#发布证书名称
dis_sign_identity="iPhone Distribution: chun xiu lin (47WKTWKMY6)"
#hoc证书名称
hoc_pp_name="lcx_ya_pp_hoc"
#hoc证书签名 SHA-1
hoc_pp_identity="DA1E926306210233BA9C75F6707B02BA2D754AC9"
#store证书名称
store_pp_name="lcx_ya_pp_store"
#store证书签名 SHA-1
store_pp_identity="DA1E926306210233BA9C75F6707B02BA2D754AC9"
#蒲公英apiKey
pgyer_api_key="0ed6b731065e8955baf8c964f478272c"
 
#打包plist文件位置
exportoptions_plist_path=./ExportOptions.plist

echo "---------------------------------开始打包---------------------------------"
#1.1 复制ExportOptions.plist到工程目录下
cp -r ./ExportOptions.plist ${project_path}
#1.2 进入项目目录
cd ${project_path}
#1.3 修改ExportOptions.plist里的provisioningProfiles(Dictionary)
/usr/libexec/PlistBuddy -c "Delete :provisioningProfiles" ${exportoptions_plist_path}
/usr/libexec/PlistBuddy -c "Add :provisioningProfiles dict" ${exportoptions_plist_path}
if [ "${archive_type}" = "hoc" ]
then
    #1.3 修改ExportOptions.plist里的provisioningProfiles(Dictionary)
    /usr/libexec/PlistBuddy -c "Add :provisioningProfiles:${target_bundleID} string ${hoc_pp_name}" ${exportoptions_plist_path}
    #1.4 修改ExportOptions.plist里的签名signingCertificate(String)
    /usr/libexec/PlistBuddy -c "Set :signingCertificate ${hoc_pp_identity}" ${exportoptions_plist_path}
    /usr/libexec/PlistBuddy -c "Set :method ad-hoc" ${exportoptions_plist_path}
elif [ "${archive_type}" = "store" ]
then
    #1.3 修改ExportOptions.plist里的provisioningProfiles(Dictionary)
    /usr/libexec/PlistBuddy -c "Add :provisioningProfiles:${target_bundleID} string ${store_pp_name}" ${exportoptions_plist_path}
    #1.4 修改ExportOptions.plist里的签名signingCertificate(String)
    /usr/libexec/PlistBuddy -c "Set :signingCertificate ${store_pp_identity}" ${exportoptions_plist_path}
    /usr/libexec/PlistBuddy -c "Set :method app-store" ${exportoptions_plist_path}
fi

#1.5 修改ExportOptions.plist里的teamID
/usr/libexec/PlistBuddy -c "Set :teamID ${cer_teamID}" ${exportoptions_plist_path}

#2.清理旧的build目录
rm -rf build

#3.清理构建目录
xcodebuild clean -xcodeproj ./$target_name/$target_name.xcodeproj -configuration $configuration_type -alltargets

if [ "${archive_type}" = "hoc" ]
then
#4.归档
xcodebuild -workspace $target_name.xcworkspace -scheme $target_name -configuration $configuration_type -archivePath build/$target_name-adhoc.xcarchive clean archive build CODE_SIGN_IDENTITY="${dis_sign_identity}" PROVISIONING_PROFILE="${hoc_pp_name}" PRODUCT_BUNDLE_IDENTIFIER="${target_bundleID}"
#5.导出IPA
xcodebuild -exportArchive -archivePath build/$target_name-adhoc.xcarchive -exportOptionsPlist $exportoptions_plist_path -exportPath build/$target_name-adhoc
#6.上传到蒲公英
curl -F "file=@build/${target_name}-adhoc/${target_name}.ipa" -F "_api_key=${pgyer_api_key}" https://www.pgyer.com/apiv2/app/upload
elif [ "${archive_type}" = "store" ]
then
#4.归档
xcodebuild -workspace $target_name.xcworkspace -scheme $target_name -configuration $configuration_type -archivePath build/$target_name-store.xcarchive clean archive build CODE_SIGN_IDENTITY="${dis_sign_identity}" PROVISIONING_PROFILE="${store_pp_name}" PRODUCT_BUNDLE_IDENTIFIER="${target_bundleID}"
#5.导出IPA
xcodebuild -exportArchive -archivePath build/$target_name-store.xcarchive -exportOptionsPlist $exportoptions_plist_path -exportPath build/$target_name-store
fi

echo "---------------------------------结束打包---------------------------------"




