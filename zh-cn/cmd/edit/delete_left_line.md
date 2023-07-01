# 删除到行首命令

### 摘要

> 从光标位置删除到行首。

### 说明

> 从光标位置删除文本到逻辑行的开头。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **删除**
\> **删除到行首**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_DELETE\_LEFT\_LINE (4302)

### 宏

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineLogical);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineLogical
>
> document.selection.Delete 1
