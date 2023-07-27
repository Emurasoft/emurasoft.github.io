# 左移一个字符命令

## 摘要

将光标向左移动一个字符。

## 说明

将光标向左移动一个字符。如果光标在行末，这个命令会将光标移动到前一行的行末。这个命令等同于按一下键盘上的向左键。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>水平移动光标
\>左移一个字符
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 向左键

## 插件命令ID

```
EEID_LEFT (4157)```

## 宏

## \[JavaScript\]

```
document.selection.CharLeft(false,1);
```

## \[VBScript\]

```
document.selection.CharLeft false,1
```
