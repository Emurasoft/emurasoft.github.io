# 在上方插入一行命令

## 摘要

在当前光标位置上方插入新的一行。

## 说明

在光标当前所在位置上方插入新的一行。

## 运行方法

- 默认菜单:插入 \>在上方插入一行
- [所有命令](../tools/all_commands):插入 \>在上方插入一行
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+ENTER

## 插件命令ID

```
EEID_LINE_OPEN_ABOVE (4195)```

## 宏

### \[JavaScript\]

```
document.selection.LineOpen(true);
```

### \[VBScript\]

```
document.selection.LineOpen true
```
