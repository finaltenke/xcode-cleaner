# 🧼 Xcode Cleaner

一個用於清理 macOS 開發環境的快取和模擬器資料的工具。

## 功能特點

- 🚀 自動清理 Xcode 相關的快取和模擬器資料
- 🔒 安全的清理機制，避免意外刪除
- ⚡ 支援自動模式，跳過確認提示

## 清理路徑

以下路徑會被清理：

- `~/Library/Developer/CoreSimulator/Devices` - 模擬器設備資料
- `~/Library/Developer/CoreSimulator/Caches/dyld` - 模擬器動態連結快取
- `~/Library/Developer/XCTestDevices` - 測試設備資料
- `~/Library/Developer/Xcode/DerivedData` - Xcode 建置快取
- `~/Library/Developer/Xcode/iOS DeviceSupport` - iOS 設備支援檔案
- `~/Library/Developer/Xcode/Archives` - Xcode 封存檔案
- `~/Library/Developer/Xcode/iOS Device Logs` - iOS 設備日誌
- `/Library/Developer/Xcode/iOS DeviceSupport` - 系統級 iOS 設備支援檔案

## 使用方式

### 一般模式（推薦）

```bash
python main.py
```

- 會詢問每個路徑的刪除確認
- 可以選擇跳過不需要清理的路徑

### 自動模式

```bash
python main.py --auto
```

- 跳過所有確認提示
- 自動清理所有路徑

## 注意事項

- ⚠️ 使用前請確保已備份重要資料
- 🔍 建議先確認要清理的路徑內容

## 系統需求

- macOS 作業系統
- Python 3.x

## 授權

MIT License
