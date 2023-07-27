# 移至行首命令

## 摘要

将光标移至当前行的行首。

## 说明

把光标移至当前行的起始位置。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>水平移动光标
\>移至行首
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL + ALT + HOME

## 插件命令ID

```
EEID_HOME (4164)```

## 宏

## \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineView);
```

## \[VBScript\]

```
document.selection.StartOfLine false,eeLineView
```
