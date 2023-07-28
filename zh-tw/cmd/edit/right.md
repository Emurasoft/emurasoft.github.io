# 右移一個字元命令

## 摘要

將游標向右移動一個字元。

## 說明

將游標向右移動一個字元。如果游標在行末，這個命令會將游標移動到下一行的起始位置。這個命令等同于按一下鍵盤上的向右鍵。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **右移一個字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 向右鍵

## 外掛程式命令ID

```
EEID_RIGHT (4156)```

## 巨集

### \[JavaScript\]

```
document.selection.CharRight(false,1);
```

### \[VBScript\]

```
document.selection.CharRight false,1
```
