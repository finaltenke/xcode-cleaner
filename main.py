import os
import shutil
import sys
import argparse
import subprocess

# 分為安全路徑與高風險路徑
safe_directories = [
    "~/Library/Developer/CoreSimulator/Devices",
    "~/Library/Developer/CoreSimulator/Caches/dyld",
    "~/Library/Developer/XCTestDevices",
    "~/Library/Developer/Xcode/DerivedData",
    "~/Library/Developer/Xcode/iOS DeviceSupport",
    "~/Library/Developer/Xcode/Archives",
    "~/Library/Developer/Xcode/iOS Device Logs",
    "~/Library/Developer/Xcode/iOS Device Logs",
    "/Library/Developer/Xcode/iOS DeviceSupport",
]

risky_directories = [
    "/Library/Developer/CoreSimulator/Profiles/Runtimes",
    "~/Library/Caches",
    "/Library/Caches",
]

def confirm_deletion(prompt, auto=False):
    if auto:
        return True
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("請輸入 y 或 n")

def open_directory(directory):
    """在 Finder 中開啟目錄"""
    directory = os.path.expanduser(directory)
    if os.path.exists(directory):
        subprocess.run(['open', directory])
        return True
    return False

def safe_delete_directory(directory, auto=False):
    directory = os.path.expanduser(directory)
    if not os.path.exists(directory):
        print(f"❎ 目錄 {directory} 不存在，跳過")
        return

    if not confirm_deletion(f"確定要刪除 {directory} 的所有內容嗎？", auto):
        print(f"跳過 {directory}")
        return

    try:
        for name in os.listdir(directory):
            full_path = os.path.join(directory, name)
            if os.path.isfile(full_path):
                os.remove(full_path)
                print(f"🗑️ 已刪除檔案: {full_path}")
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path, ignore_errors=True)
                print(f"🧹 已刪除目錄: {full_path}")
        print(f"✅ 清理完成: {directory}\n")
    except Exception as e:
        print(f"⚠️ 刪除 {directory} 時發生錯誤: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='🧼 Xcode Cleaner - macOS 開發環境清理工具')
    parser.add_argument('--auto', action='store_true', help='自動模式：跳過所有確認提示')
    args = parser.parse_args()

    print("🧼 Xcode Cleaner - macOS 開發環境清理工具")
    print("=" * 50)
    print("⚠️  警告：此工具將刪除指定的快取與模擬器資料")
    print("請先備份重要內容！\n")

    if not args.auto and not confirm_deletion("👉 是否要繼續執行安全清理？"):
        print("已取消操作")
        sys.exit(0)

    # 清理安全路徑
    for directory in safe_directories:
        safe_delete_directory(directory, args.auto)

    # 顯示高風險路徑
    print("\n⚠️ 以下為風險較高的路徑，請自行確認後再決定是否刪除：")
    print("=" * 50)
    for directory in risky_directories:
        expanded_dir = os.path.expanduser(directory)
        if os.path.exists(expanded_dir):
            print(f"📁 {expanded_dir}")
            if not args.auto:
                if confirm_deletion(f"👉 是否要在 Finder 中開啟此目錄？"):
                    if open_directory(expanded_dir):
                        print(f"✅ 已在 Finder 中開啟：{expanded_dir}")
                    else:
                        print(f"❌ 無法開啟目錄：{expanded_dir}")
        else:
            print(f"❎ 目錄不存在：{expanded_dir}")
        print("-" * 50)

if __name__ == "__main__":
    main()
