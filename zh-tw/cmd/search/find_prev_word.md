# 尋找上一單字命令

## 摘要

尋找目前的單字的前一個符合結果。

## 說明

如果已經選取一個字串的話，尋找符合指定字串的下一個符合結果。否則，尋找與游標處的單字元合的下一個符合結果。

## 運行方法

- 預設功能表: **搜索** \> **尋找上一單字**
- [全部命令](../tools/all_commands): **搜索**
\> **尋找上一單字**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: CTRL+SHIFT+F3

## 外掛程式命令ID

```
EEID_FIND_PREV_WORD (4205)```

## 巨集

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatPrevious \| eeFindRepeatWord);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatPrevious Or eeFindRepeatWord
```
