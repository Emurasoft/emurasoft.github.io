# 符合整個單字 (搜尋工具列) 命令

### 摘要

> 切換搜尋工具列上「符合整個單字」按鈕的狀態。

### 說明

> 切換搜尋工具列上「符合整個單字」按鈕的狀態。當這個命令被切換時，搜尋會返回只有當整個單字都符合的搜尋結果。
> (例如，"searches" 將不會是 "search"的符合的結果。)

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **搜尋**
\> **搜尋工具列** \> **符合整個單字**
- 工具列: ![](../../images/find_only_word.png) (搜尋工具列)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FINDBAR\_ONLY\_WORD (4576)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4576);

#### \[VBScript\]

> editor.ExecuteCommandByID 4576
