# 尋找上一個命令

## 摘要

尋找上一個符合。

## 說明

用同樣的參數尋找與之前搜尋過的字串相同的上一個符合。

## 運行方法

- 預設功能表: **搜尋** \> **上一個**
- [全部命令](../tools/all_commands): **搜尋**
\> **上一個**
- Toolbar:
![](../../images/editrepeatback.png)
- 狀態列: 無
- 預設捷徑: SHIFT+F3

## 外掛程式命令ID

```
EEID_EDIT_REPEAT_BACK (4203)
```

## 巨集

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatPrevious);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatPrevious
```
