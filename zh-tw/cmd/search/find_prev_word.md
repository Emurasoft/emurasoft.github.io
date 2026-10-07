# 尋找上一個字命令

## 摘要

尋找指定文字的前一個符合結果。

## 說明

如果已經選取一個字串的話，尋找符合指定字串的下一個符合結果。否則，尋找與游標處的單字元合的下一個符合結果。

## 運行方法

- 預設功能表: **搜尋** \> **尋找上一個字**
- [全部命令](../tools/all_commands): **搜尋** \> **尋找/取代** \> **尋找上一個字**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: CTRL+SHIFT+F3

## 外掛程式命令ID

```
EEID_FIND_PREV_WORD (4205)```

## 巨集

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatPrevious | eeFindRepeatWord);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatPrevious Or eeFindRepeatWord
```
