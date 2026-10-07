# 儲存工作區與所有檔案並全部關閉命令

## 摘要

儲存該工作區,儲存並關閉所有開啟的檔案。

## 說明

這個命令儲存工作區以及所有打開的文檔，然后再關閉所有打開的文檔。這個命令等同于 [儲存預設工作區命令](save_workspace) 加 [儲存并關閉命令](save_exit_all)。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **關閉** \> **儲存工作區與所有檔案並全部關閉**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_SAVE_WORKSPACE_EXIT_ALL (4331)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4331);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4331
```
