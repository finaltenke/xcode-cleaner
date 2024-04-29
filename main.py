import os
import shutil

# 定義要刪除的目錄列表
directories = [
    # 存放所有曾經開過的模擬器（各種版本的模擬器），都會在這裡開一個專用的 Folder 存放，可以全部刪除
    "~/Library/Developer/CoreSimulator/Devices",
    #
    # delete each directory
    # "~/Library/Developer/CoreSimulator/Caches/dyld",
    #
    # "~/Library/Developer/XCTestDevices",
    #
    # 這裡存放所有 build 過的 app 的檔案，可以全部刪除
    # "~/Library/Developer/Xcode/DerivedData",
    #
    # Mac 電腦連接過的 iOS 設備( iPhone/iPad...)，就會在這裡產生一個 folder ，一個 folder 可能占用多達 2GB+，可以隨時刪除
    # "~/Library/Developer/Xcode/iOS DeviceSupport",
    #
    # delete each directory
    # "~/Library/Developer/Xcode/Archives",
    #
    # delete each directory
    # "~/Library/Developer/Xcode/iOS Device Logs",
    #
    # delete each directory
    "~/Library/Caches",
    #
    # Mac 電腦連接過的 iOS 設備( iPhone/iPad...)，就會在這裡產生一個 folder ，一個 folder 可能占用多達 2GB+，可以隨時刪除
    # "/Library/Developer/Xcode/iOS DeviceSupport",
    #
    # Simulator runtime
    "/Library/Developer/CoreSimulator/Profiles/Runtimes",
    #
    # delete each directory
    # "/Library/Caches",
]

# 對於每個目錄，檢查它是否存在
for directory in directories:
    directory = os.path.expanduser(directory)  # 處理帶有 ~ 的路徑
    if os.path.exists(directory):
        # 如果目錄存在，則刪除它下面的所有檔案和子目錄
        for name in os.listdir(directory):
            full_path = os.path.join(directory, name)
            if os.path.isfile(full_path):
                os.remove(full_path)
                print(f"Deleted {full_path}")
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path, ignore_errors=True)
                print(f"Deleted {full_path}")
    else:
        # 如果目錄不存在，則跳過並繼續下一個
        print(f"Directory {directory} does not exist, skipping")
