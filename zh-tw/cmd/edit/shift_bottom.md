# 延伸選取到文件底部命令

## 摘要

將選區延伸到目前的文件底部。

## 說明

把選區延伸到文檔底部。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選取** \> **延伸選取到文件底部**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+END

## 外掛程式命令ID

```
EEID_SHIFT_BOTTOM (4185)```

## 巨集

### \[JavaScript\]

```
document.selection.EndOfDocument(true);
```

### \[VBScript\]

```
document.selection.EndOfDocument true
```
