# 插入 CR 命令

### 摘要

> 在光标处插入 CR。

### 说明

> 在当前光标位置处插入一个回车(CR)。EmEditor可以编辑同时有 CR 和 LF 作为换行的文件。按一下回车键(ENTER)在当前行插入相同的换行方式，仅 CR，仅 LF，或 CR+LF。这个命令会一直插入仅 CR 的换行方式，无论在当期行使用的是哪一种换行方式。

### 运行方法

- 默认菜单: **插入** \> **仅 CR**
- [所有命令](../tools/all_commands): **插入** \> **仅 CR**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_INSERT\_CR (4145)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4145);

#### \[VBScript\]

> editor.ExecuteCommandByID 4145
