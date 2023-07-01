# 小写命令

### 摘要

> 把选定文本全部转换为小写字符。

### 说明

> 把选定文本全部转换为小写字符。例如，A 会变成 a, Ä
> 会变成 ä，还有 Λ 会变成 λ.

### 运行方法

- 默认菜单: **转换** \> **小写**
- [所有命令](../tools/all_commands): **转换** \> **小写**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+U

### 插件命令ID

- EEID\_MAKE\_LOWER (4150)

### 宏

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseLowerCase);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseLowerCase
