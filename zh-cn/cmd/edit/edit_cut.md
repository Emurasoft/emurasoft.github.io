# 剪切命令

## 摘要

剪切选定内容或当前行至剪贴板。

## 说明

剪切选取的文本并把它放到剪贴板上。在这个指令之后，你可以通过把光标移动到另一个地方并且运行 [粘贴 指令](edit_paste) 来放置选取内容。

## 运行方法

- 默认菜单:编辑 \>剪切
- [所有命令](../tools/all_commands):编辑 \>剪切 \>剪切
- 工具栏: ![](../../images/cut.gif)
- 状态栏: 无
- 默认快捷键: CTRL+X 或 SHIFT+DELETE

## 插件命令ID

```
EEID_EDIT_CUT (4126)```

## 宏

### \[JavaScript\]

```
document.selection.cut();
```

### \[VBScript\]

```
document.selection.Cut
```
