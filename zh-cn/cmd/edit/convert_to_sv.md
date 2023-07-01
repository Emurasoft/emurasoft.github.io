# 转换为 CSV (多个条目) 命令

### 摘要

> 把当前含有分隔值的文档或固定列宽文档转换为指定的分隔值文档 (多个条目)。

### 说明

> 把当前含有分隔值的文档或固定列宽文档转换为指定的分隔值文档。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **CSV** \> **转换为** \> **(CSV 格式)**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令 ID

- 从 EEID\_CONVERT\_TO\_SV 到 EEID\_CONVERT\_TO\_SV + 63 (从 22656 到 22656 + 63)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(22656 + i); //i 是一个从 0 到 63 的整数

#### \[VBScript\]

> editor.ExecuteCommandByID 22656 + i 'i 是一个从 0 到 63 的整数
