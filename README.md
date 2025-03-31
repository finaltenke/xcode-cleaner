# 🧼 Xcode Cleaner

一個用於清理 macOS 開發環境的快取和模擬器資料的工具。

## 功能特點

- 🚀 自動清理 Xcode 相關的快取和模擬器資料
- 🔒 分為安全路徑和高風險路徑
- 👀 高風險路徑提供 Finder 預覽功能
- ⚡ 支援自動模式，跳過確認提示
- 🛡️ 高風險路徑需要手動確認，避免意外刪除

## 安全路徑（自動清理）

以下路徑會被自動清理：

- `~/Library/Developer/CoreSimulator/Devices` - 模擬器設備資料
- `~/Library/Developer/CoreSimulator/Caches/dyld` - 模擬器動態連結快取
- `~/Library/Developer/XCTestDevices` - 測試設備資料
- `~/Library/Developer/Xcode/DerivedData` - Xcode 建置快取
- `~/Library/Developer/Xcode/iOS DeviceSupport` - iOS 設備支援檔案
- `~/Library/Developer/Xcode/Archives` - Xcode 封存檔案
- `~/Library/Developer/Xcode/iOS Device Logs` - iOS 設備日誌
- `/Library/Developer/Xcode/iOS DeviceSupport` - 系統級 iOS 設備支援檔案

## 高風險路徑（手動確認）

以下路徑需要手動確認：

- `/Library/Developer/CoreSimulator/Profiles/Runtimes` - 模擬器運行時
- `~/Library/Caches` - 使用者快取目錄
- `/Library/Caches` - 系統快取目錄

## 使用方式

### 一般模式（推薦）

```bash
python main.py
```

- 會詢問每個安全路徑的刪除確認
- 顯示高風險路徑並提供 Finder 預覽選項
- 高風險路徑需要手動處理

### 自動模式

```bash
python main.py --auto
```

- 跳過所有確認提示
- 自動清理安全路徑
- 仍然會顯示高風險路徑，但不會詢問是否開啟

## 注意事項

- ⚠️ 使用前請確保已備份重要資料
- 🔍 高風險路徑建議先查看內容再決定是否刪除
- 🚫 高風險路徑不會自動刪除，需要手動處理

## 系統需求

- macOS 作業系統
- Python 3.x

## 授權

MIT License
