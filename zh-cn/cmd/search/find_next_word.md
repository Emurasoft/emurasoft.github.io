# 查找下一单词命令

### 摘要

> 查找当前单词的下一个匹配结果。

### 说明

> 如果已经选取一个字符串的话，查找符合指定字符串的下一个匹配结果。否则，查找与光标处的单词符合的下一个匹配结果。

### 运行方法

- 默认菜单: **搜索** \> **查找下一单词**
- [所有命令](../tools/all_commands): **搜索**
\> **查找下一单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: Ctrl+F3

### 插件命令ID

- EEID\_FIND\_NEXT\_WORD (4204)

### 宏

#### \[JavaScript\]

> document.selection.FindRepeat(eeFindRepeatNext \| eeFindRepeatWord);

#### \[VBScript\]

> document.selection.FindRepeat eeFindRepeatNext Or eeFindRepeatWord