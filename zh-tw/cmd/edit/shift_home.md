# 延伸選區到行首命令

## 摘要

把選區延伸到目前的行的行首。

## 說明

把選區延伸到目前的行的行首。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **延伸選區到行首**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_SHIFT_HOME (4180)```

## 巨集

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineView);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineView
```
