# 延伸選取到符合的括弧命令

## 摘要

延伸選取到相應的括弧。

## 說明

當游標在一個左或右圓括號或方括號處，這個命令會把選區延伸到相對應的右或左圓括號或方括號處。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選取** \> **延伸選取到符合的括弧**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+\]

## 外掛程式命令ID

```
EEID_SHIFT_NEXT_PAREN (4277)```

## 巨集

### \[JavaScript\]

```
document.selection.GoToBrace(true);
```

### \[VBScript\]

```
document.selection.GoToBrace true
```
