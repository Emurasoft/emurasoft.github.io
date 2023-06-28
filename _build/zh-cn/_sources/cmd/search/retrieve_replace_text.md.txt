# 设置单词为替换字符串命令

### 摘要

> 设置当前光标所在的单词为替换字符串。

### 说明

> 设置当前光标所在处的单词为替换字符串，并用于为 [**替换下一个** 命令](replace_next)。在执行这个命令之后，如果你再选择 [**替换下一个** 命令](replace_next)，它会马上用该命令所指定的单词替换下一个查询单词。如果在如果在 [**替换** 对话框](../../dlg/replace/index) 中 **「>」按钮** 下的菜单中选择了“自定义”，那么 [**替换** 对话框](../../dlg/replace/index) 会默认把用这个命令指定的单词作为替换字符串。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **搜索**
\> **设置单词为替换字符串**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_RETRIEVE\_REPLACE\_TEXT (4446)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4446);

#### \[VBScript\]

> editor.ExecuteCommandByID 4446