# 设置单词为查找字符串命令

## 摘要

把当前单词设置为查询字符串。

## 说明

设置当前光标所在处的单词为查询字符串，并用于为 [查找下一个 命令](edit_repeat)。在执行这个命令之后，如果你再选择 [查找下一个 命令](edit_repeat)，它会马上查找下一个与用该命令所指定的单词匹配的结果。如果在 [查找 对话框](../../dlg/find/index) 中「>」按钮 下的菜单中没有勾选“光标下的单词”，那么 [查找 对话框](../../dlg/find/index) 会默认把用这个命令指定的单词作为查找字符串。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):搜索
\>设置单词为查找字符串
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_RETRIEVE_FIND_TEXT (4325)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4325);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4325
```
