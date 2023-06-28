# 配置列表命令

### 摘要

> 选择一个指定的配置（多个项目）。

### 说明

> 这个命令有多个菜单项目组成。这个命令选择指定的配置作为当前配置。当前的配置会被显示在状态栏中。EmEditor 默认的配置为 **文本** 配置当新建一个文档时。

### 运行方法

- 默认菜单: **工具** \> **选择配置** \> （ **配置名称**）
- [所有命令](all_commands): **工具** >
**选择配置** \> （ **配置名称**）
- 工具栏: ![](../../images/configpopup.gif)（点击箭头） \> （ **配置名称**）
- 状态栏: （双击配置名称） \> （ **配置名称**）
- 默认快捷键: 无

### 插件命令ID

- From EEID\_SELECT\_CONFIG through EEID\_SELECT\_CONFIG + 255 （从 5120 到 5120 + 255）

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(5120 + i);  // i 是从 0 到 255 的整数
>
> ##### or
>
> document.ConfigName = "（配置名称）";

#### \[VBScript\]

> editor.ExecuteCommandByID 5120 + i   ' i 是从 0 到 255 的整数
>
> ##### or
>
> document.ConfigName = "（配置名称）"