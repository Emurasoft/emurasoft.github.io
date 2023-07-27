# 保存默认工作区命令

## 摘要

保存默认工作区。

## 说明

这个命令会保存所有目前在 EmEditor 中打开的文档的完整的路径名称，光标位置，以及其他设定。 [还原默认工作区 命令](load_workspace) 则会还原通过这个命令保存的位置与设定。

## 运行方法

- 默认菜单:系统托盘图标菜单 \>保存默认工作区
- [所有命令](../tools/all_commands):文件 \>工作区
\>保存默认工作区
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+0

## 插件命令ID

```
EEID_SAVE_WORKSPACE (4330)```

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(4330);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4330
```
