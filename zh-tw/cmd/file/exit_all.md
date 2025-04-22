# 全部關閉命令

## 摘要

關閉打所有開的檔案。

## 說明

這個命令會關閉所有已打開的檔案。如果存在一個已被修改的文檔，則會顯示一個即時消息來讓您選擇是否想要儲存變更。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **關閉**
\> **全部關閉**
- 工具列: ![](../../images/exitall.png)
- 狀態列: 無
- 預設捷徑: ALT+SHIFT+X

## 外掛程式命令ID

```
EEID_EXIT_ALL (4119)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4119);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4119
```
