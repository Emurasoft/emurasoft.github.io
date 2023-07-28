# 复制引用并取消选择命令

## 摘要

将所选内容复制引用，粘贴至剪贴板并取消选择。

## 说明

将所选内容复制为引用文本，粘贴至剪贴板并取消选择所选内容。这个命令等同于 [**复制引用** 命令](edit_copy_prefix) 加 [**取消选取** 命令](escape)。 在这个指令之后，你可以通过移动光标到不同的位置再运行 [**粘贴** 命令](edit_paste) 来放置选取内容。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **复制**
\> **复制引用并取消选择**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+Q

## 插件命令ID

```
EEID_EDIT_COPY_PREFIX_DESELECT (4131)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID (4131);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4131
```
