# 新增並貼為引用文字命令

## 摘要

建立一個新的檔案並把剪貼簿內容貼為引用文字。

## 說明

這個命令等同于 [**新文字檔** 命令](file_new) 加 [**貼為引用文字** 命令](../edit/paste_prefix)。在預設設置下，新增的檔案會使用文字(Text)組態。您可以到 [**定義組態** 對話方塊](../../dlg/configurations/index) 中更改這個預設組態。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **新增** \> **新增檔案並貼為引文**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_NEW_PASTE_PREFIX (4271)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4271);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4271
```
