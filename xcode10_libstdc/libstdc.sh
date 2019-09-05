

target_path_1="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot/usr/lib/"
target_path_2="/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/lib/"
target_path_3="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/lib/"
target_path_4="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/usr/lib/"

sudo cp -r ./1/libstdc++.dylib ${target_path_1}
sudo cp -r ./1/libstdc++.6.dylib ${target_path_1}
sudo cp -r ./1/libstdc++.6.0.9.dylib ${target_path_1}

sudo cp -r ./2/libstdc++.tbd ${target_path_2}
sudo cp -r ./2/libstdc++.6.tbd ${target_path_2}
sudo cp -r ./2/libstdc++.6.0.9.tbd ${target_path_2}

sudo cp -r ./3 ${target_path_3}
sudo cp -r ./3/libstdc++.6.tbd ${target_path_3}
sudo cp -r ./3/libstdc++.6.0.9.tbd ${target_path_3}

sudo cp -r ./4 ${target_path_4}
sudo cp -r ./4/libstdc++.6.tbd ${target_path_4}
sudo cp -r ./4/libstdc++.6.0.9.tbd ${target_path_4}

