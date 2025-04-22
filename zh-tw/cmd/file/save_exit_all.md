# 儲存并全部關閉命令

## 摘要

儲存并關閉所有打開的檔案。

## 說明

儲存并關閉所有打開的檔案。這個命令等同于 [**全部儲存** 命令](file_save_all) 加 [**全部關閉** 命令](exit_all)。

## 運行方法

- 預設功能表: **檔案** \> **儲存并全部關閉**
- [全部命令](../tools/all_commands): **檔案** \> **關閉**
\> **儲存并全部關閉**
- 工具列: ![](../../images/saveexitall..png)
- 狀態列: 無
- 預設捷徑: CTRL+SHIFT+E

## 外掛程式命令ID

```
EEID_SAVE_EXIT_ALL (4118)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4118);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4118
```
