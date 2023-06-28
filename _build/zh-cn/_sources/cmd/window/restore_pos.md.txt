# 还原窗口位置命令

### 摘要

> 将窗口还原到上次保存的位置。

### 说明

> 该命令会把窗口还原到之前保存过的位置。在使用这个命令之前，窗口位置必须先通过 **「保存当前窗口位置」** 按钮被保存；该按钮位于 [**自定义** 对话框](../../dlg/customize/index) 中 [**窗口** 页面](../../dlg/customize/window/index) 上。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **窗口**
\> **还原** \> **还原窗口位置**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL + 9

### 插件命令 ID

- EEID\_RESTORE\_POS (4406)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4406);

#### \[VBScript\]

> editor.ExecuteCommandByID 4406