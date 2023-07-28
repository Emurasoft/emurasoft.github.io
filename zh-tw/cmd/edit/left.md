# 左移一個字元命令

## 摘要

將游標向左移動一個字元。

## 說明

將游標向左移動一個字元。如果游標在行末，這個命令會將游標移動到前一行的行末。這個命令等同于按一下鍵盤上的向左鍵。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **左移一個字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 向左鍵

## 外掛程式命令ID

```
EEID_LEFT (4157)```

## 巨集

### \[JavaScript\]

```
document.selection.CharLeft(false,1);
```

### \[VBScript\]

```
document.selection.CharLeft false,1
```
