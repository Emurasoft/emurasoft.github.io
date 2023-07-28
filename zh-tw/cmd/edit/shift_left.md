# 往左延伸一個字元命令

## 摘要

把選區往左延伸一個字元。

## 說明

把選區往左延伸一個字元。如果游標在行的開頭，這個命令會把游標移到上一行的末尾。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **往左延伸一個字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT + LEFT ARROW

## 外掛程式命令ID

```
EEID_SHIFT_LEFT (4173)```

## 巨集

### \[JavaScript\]

```
document.selection.CharLeft(true,1);
```

### \[VBScript\]

```
document.selection.CharLeft true,1
```
