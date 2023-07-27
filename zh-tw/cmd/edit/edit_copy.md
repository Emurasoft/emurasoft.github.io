# 複製命令

## 摘要

複製選定內容或目前的行到剪貼簿。

## 說明

複製選取的文字并把它放到剪貼簿上。在這個指示詞之後，您可以通過把游標移動到另一個地方并且運行 [貼上 指示詞](edit_paste) 來放置選取內容。

## 運行方法

- 預設功能表:編輯 \>複製
- [全部命令](../tools/all_commands):編輯 \>複製 \>複製
- 工具列: ![](../../images/copy.gif)
- 狀態列: 無
- 預設捷徑: CTRL+C 或 CTRL+INSERT

## 外掛程式命令ID

```
EEID_EDIT_COPY (4127)```

## 巨集

### \[JavaScript\]

```
document.selection.Copy(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Copy eeCopyUnicode
```
