# 儲存預設工作區命令

## 摘要

儲存預設工作區。

## 說明

這個命令會儲存目前所有在 EmEditor 中打開的文檔的完整的路徑名稱，游標位置，以及其他設定。 [還原預設工作區 命令](load_workspace) 則會還原通過這個命令儲存的位置與設定。

## 運行方法

- 預設功能表:系統系統匣圖示功能表 \>儲存預設工作區
- [全部命令](../tools/all_commands):檔案 \>工作區
\>儲存預設工作區
- 工具列: 無
- 狀態列: 無
- 預設捷徑: CTRL+SHIFT+0

## 外掛程式命令ID

```
EEID_SAVE_WORKSPACE (4330)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4330);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4330
```
