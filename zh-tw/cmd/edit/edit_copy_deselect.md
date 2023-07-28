# 複製並取消選擇命令

## 摘要

複製所選內容到剪貼簿並取消選擇所選內容。

## 說明

複製選取的文字到剪貼簿上并取消選擇所選文字。這個命令等同于 [**複製** 命令](edit_copy) 加 [**取消選擇** 命令](escape)。在這個命令之後，您可以通過把游標移動到不同的位置再運行 [**貼上** 命令](edit_paste) 來放置選取內容。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **複製**
\> **複製並取消選擇**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+C

## 外掛程式命令ID

```
EEID_EDIT_COPY_DESELECT (4128)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4128);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4128
```
