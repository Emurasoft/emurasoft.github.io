# 日期和时间命令

### 摘要

> 插入日期与时间。

### 说明

> 在光标位置处插入当前日期和时间。这个命令会先插入日期，接着一个空格，跟着是时间。插入的日期与时间的格式可以在 Windows 系统上配置。在 **控制面板** 中选择 **区域和语言选项**，然后选择 **日期和时间**。

### 运行方法

- 默认菜单: **插入** \> **日期和时间**
- [所有命令](../tools/all_commands): **插入** \> **日期和时间**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+F5

### 插件命令ID

- EEID\_INSERT\_DATE\_TIME (4138)

### 宏

#### \[JavaScript\]

> document.selection.InsertDate(eeDateDateTime);

#### \[VBScript\]

> document.selection.InsertDate eeDateDateTime
