# 循环粘贴命令

## 摘要

在光标位置处插入剪贴板中的历史内容。

## 说明

在光标处插入剪贴板中的历史内容（即最近复制的项目）。重复选择这个命令会循环剪贴板历史记录中的项目。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>粘贴
\>循环粘贴
- 工具栏: ![](../../images/cycle_clipboard_ring.gif)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_PASTE_HISTORY (4454)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4454);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4454
```
