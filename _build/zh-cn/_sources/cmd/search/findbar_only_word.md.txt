# 匹配整个单词 (查找工具栏) 命令

### 摘要

> 切换查找工具栏上「匹配整个单词」按钮的状态。

### 说明

> 切换查找工具栏上「匹配整个单词」按钮的状态。当这个命令被切换时，搜索会返回只有当整个单词都匹配的搜索结果。
> (例如，"searches" 将不会是 "search"的匹配结果。)

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **搜索**
\> **查找工具栏** \> **匹配整个单词**
- 工具栏: ![](../../images/find_only_word.png) (查找工具栏)
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_FINDBAR\_ONLY\_WORD (4576)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4576);

#### \[VBScript\]

> editor.ExecuteCommandByID 4576