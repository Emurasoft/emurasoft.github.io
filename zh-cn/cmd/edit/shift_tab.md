# 左移制表符或减少行缩进命令

## 摘要

将光标向左移动一个制表符或减少行缩进。

## 说明

将光标向左移动一个制表符（tab字符）。如果多行被选取了，这个命令会减少所有选取行行首的缩进通过删除一个制表符或同等的空格数。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>水平移动光标
\>移除制表符或减少行缩进
Indent
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SHIFT_TAB (4189)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4189);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4189
```
