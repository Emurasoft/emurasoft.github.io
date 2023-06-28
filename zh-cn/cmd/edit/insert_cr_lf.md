# 插入CR与LF命令

### 摘要

> 在光标位置插入回车与换行。

### 说明

> 在当前光标位置处插入一个回车(CR)和一个换行符(LF)。EmEditor可以编辑同时有CR和LF作为换行的文件。按一下回车键(ENTER)在当前行插入相同的换行方式，仅CR，仅LF，或CR+LF。这个命令会一直插入CR+LF的换行方式，无论在当期行使用的是哪一种换行方式。

### 运行方法

- 默认菜单: **插入** \> **CR与LF**
- [所有命令](../tools/all_commands): **插入** \> **CR与LF**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_INSERT\_CR\_LF (4274)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4274);

#### \[VBScript\]

> editor.ExecuteCommandByID 4274