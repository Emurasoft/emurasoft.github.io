# 文档列表命令

### 摘要

> 切换到指定的文档（多个项目）。

### 说明

> 切换到指定的 EmEditor 文档。如果指定的文档被最小化了，这个命令会还原指定文档的正常大小。这个命令由多个菜单项目组成。

### 运行方法

- 默认菜单: **窗口** \> （ **文档名称**）
- [所有命令](../tools/all_commands): **窗口**
\> （ **文档名称**）
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令 ID

- 从 EEID\_WINDOW\_MENU 到 EEID\_WINDOW\_MENU + 255 （从 5376 到 5376 + 255）

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(5376 + i);  // i是一个从0到255的整数

#### \[VBScript\]

> editor.ExecuteCommandByID 5376 + i   ' i是一个从0到255的整数
