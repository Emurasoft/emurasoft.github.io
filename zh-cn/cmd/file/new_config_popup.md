# 新建（弹出菜单）命令

### 摘要

> 显示一个弹出菜单来使用指定的配置新建一个文件。

### 说明

> 这个命令会显示一个新的 EmEditor 窗口并准备一个新的文档。该命令将不会立即在磁盘上创建新文件。该文件会在你输入并选择 [**保存** 命令](file_save) 或 [**另存为** 命令](file_save_as) 之后才会被创建。
>
> 这个命令会显示一个弹出菜单，并让你选择新建文件的配置 (例如，Text，HTML，VBScript 等等)。如果指定的配置被配置成模板文件，该模板会被用作起始文档。一个模板文件，新文件的编码，换行方式以及字体类别都能在 [**新建文件详细信息** 对话框](../../dlg/properties/file/new_details/index) 中设置。要打开该对话框，可以到点击 [**当前配置属性** 按钮](../tools/customize) (或按 ALT + ENTER)，选择 [**文件** 页面](../../dlg/properties/file/index)，然后点击 **新建文件** 按钮。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **新建** \> **新建 (弹出菜单)**
- 工具栏: ![](../../images/filenew.gif) (点击箭头)
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_NEW\_CONFIG\_POPUP (4281)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4281);

#### \[VBScript\]

> editor.ExecuteCommandByID 4281