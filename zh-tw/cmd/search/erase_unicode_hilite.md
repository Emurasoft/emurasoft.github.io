# 清除 Unicode 亮顯命令

## 摘要

清除無法為儲存進行編碼轉換的 Unicode 字元的亮顯。

## 說明

為被搜尋的無法轉換為要儲存的編碼 Unicode 字元重設亮顯。這個命令還能重設用 [**尋找下一個 Unicode 字元** 命令](find_next_unicode) 或 [**尋找上一個 Unicode 字元** 命令](find_prev_unicode) 設定的要儲存的編碼。

## 運行方法

- 預設功能表: **搜尋** \> **取消 Unicode 醒目提示**
- [全部命令](../tools/all_commands): **搜尋** \> **Unicode** \> **取消 Unicode 醒目提示**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: ALT+F9

## 外掛程式命令ID

```
EEID_ERASE_UNICODE_HILITE (4377)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4377);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4377
```
