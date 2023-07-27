# 复制链接命令

## 摘要

复制一个超链接到剪贴板。

## 说明

复制光标处的一个超链接字符串并把它粘贴到剪贴板上。在这个指令之后，你可以通过把光标移动到另一个地方并运行 [粘贴 命令](edit_paste) 来放置选取内容。

## 运行方法

- 默认菜单:编辑 \>复制链接
- [所有命令](../tools/all_commands):编辑 \>复制
\>复制链接
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_EDIT_COPY_LINK (4140)```

## 宏

### \[JavaScript\]

```
document.selection.CopyLink();
```

### \[VBScript\]

```
document.selection.CopyLink
```
