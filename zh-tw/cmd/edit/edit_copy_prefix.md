# 複製為引用文字命令

## 摘要

複製所選內容為引用文字並貼上到剪貼簿。

## 說明

與每行開頭的引用符號一起復制所選文字并把它放到剪貼簿上。在這個命令之後，您可以通過移動游標到不同的位置再運行 [貼上 命令](edit_paste) 來放置所選內容。

## 運行方法

- 預設功能表:編輯 \>複製引用
- [全部命令](../tools/all_commands):編輯 \>複製
\>複製引用
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_EDIT_COPY_PREFIX (4130)```

## 巨集

### \[JavaScript\]

```
document.selection.Copy(eeCopyQuotes);
```

### \[VBScript\]

```
document.selection.Copy eeCopyQuotes
```
