# 复制并取消选择命令

## 摘要

复制所选内容到剪贴板并取消选择所选内容。

## 说明

复制选取的文本到剪贴板上并取消选择所选文本。这个命令等同于 [复制 命令](edit_copy) 加 [取消选择 命令](escape)。在这个命令之后，你可以通过移动光标到不同的位置再运行 [粘贴 指令](edit_paste) 来放置选取内容。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>复制
\>复制并取消选择
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+C

## 插件命令ID

```
EEID_EDIT_COPY_DESELECT (4128)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4128);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4128
```
