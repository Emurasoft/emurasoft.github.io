# 插入 LF 命令

### 摘要

> 在光标处插入 LF。

### 说明

> 在当前光标位置处插入一个换行符(LF)。EmEditor可以编辑同时有 CR 和 LF 作为换行的文件。按一下回车键(ENTER)在当前行插入相同的换行方式，仅 CR，仅 LF，或 CR+LF。这个命令会一直插入仅 LF 的换行方式，无论在当期行使用的是哪一种换行方式。

### 运行方法

- 默认菜单: **插入** \> **仅 LF**
- [所有命令](../tools/all_commands): **插入** \> **仅 LF**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_INSERT\_LF (4146)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4146);

#### \[VBScript\]

> editor.ExecuteCommandByID 4146
