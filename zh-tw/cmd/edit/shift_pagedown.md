# 延伸選區到下一頁命令

## 摘要

把選區向下延伸一頁。

## 說明

把選區向下延伸一頁。如果組態屬性對話方塊中的 [**捲動** 頁面](../../dlg/properties/scroll/index) 上的 **捲動半頁** 核取方塊被勾選的話，游標只會移動半頁。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **垂直移動游標**
\> **延伸選區到下一頁**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+PAGE DOWN

## 外掛程式命令ID

```
EEID_SHIFT_PAGEDOWN (4179)```

## 巨集

### \[JavaScript\]

```
document.selection.PageDown(true,1);
```

### \[VBScript\]

```
document.selection.PageDown true,1
```
