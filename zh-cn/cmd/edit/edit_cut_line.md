# 剪切行命令

## 摘要

剪切选取的行或当前行至剪贴板。

## 说明

剪切选取的行或光标处的一逻辑行，并把它放到剪贴板中。在这个指令之后，你可以通过把光标移动到另一个地方并运行 [**粘贴** 命令](edit_paste) 来放置该行。

## 运行方法

- 默认菜单: **编辑** \> **高级** \> **剪切行**
- [所有命令](../tools/all_commands): **编辑** \> **剪切**
\> **剪切行**
- 工具栏:无
- 状态栏:无
- 默认快捷键: CTRL+L

## 插件命令ID

```
EEID_EDIT_CUT_LINE (4193)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4193);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4193
```
