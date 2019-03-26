target_path_1="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot/usr/lib/"
target_path_2="/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/lib/"
target_path_3="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/lib/"
target_path_4="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/usr/lib/"

cd 1
sudo cp -r ./libstdc++.6.0.9.dylib ${target_path_1}
sudo cp -r ./libstdc++.6.dylib ${target_path_1}
sudo cp -r ./libstdc++.dylib ${target_path_1}
cd ..

cd 2
sudo cp -r ./libstdc++.6.0.9.dylib ${target_path_2}
sudo cp -r ./libstdc++.6.dylib ${target_path_2}
sudo cp -r ./libstdc++.dylib ${target_path_2}
cd ..

cd 3
sudo cp -r ./libstdc++.6.0.9.dylib ${target_path_3}
sudo cp -r ./libstdc++.6.dylib ${target_path_3}
sudo cp -r ./libstdc++.dylib ${target_path_3}
cd ..

cd 4
sudo cp -r ./libstdc++.6.0.9.dylib ${target_path_4}
sudo cp -r ./libstdc++.6.dylib ${target_path_4}
sudo cp -r ./libstdc++.dylib ${target_path_4}
cd ..
