# 扩展选区到文档底部命令

### 摘要

> 把选区扩展到文档底部。

### 说明

> 把选区扩展到文档底部。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到文档底部**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+END

### 插件命令ID

- EEID\_SHIFT\_BOTTOM (4185)

### 宏

#### \[JavaScript\]

> document.selection.EndOfDocument(true);

#### \[VBScript\]

> document.selection.EndOfDocument true