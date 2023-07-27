# 剪下行命令

## 摘要

剪下選取的行或目前的行到剪貼簿。

## 說明

剪下選取的行或游標處的一邏輯行，并把它放到剪貼簿中。在這個指示詞之後，您可以通過把游標移動到另一個地方并運行 [貼上 命令](edit_paste) 來放置該行。

## 運行方法

- 預設功能表:編輯 \>進階 \>剪下行
- [全部命令](../tools/all_commands):編輯 \>剪下
\>剪下行
- 工具列:無
- 狀態列:無
- 預設鍵盤快速鍵: CTRL+L

## 外掛程式命令ID

```
EEID_EDIT_CUT_LINE (4193)```

## 巨集

### \[JavaScript\]

```
document.selection.SelectLine()
document.selection.Cut();
```

### \[VBScript\]

```
document.selection.SelectLine
document.selection.Cut
```
