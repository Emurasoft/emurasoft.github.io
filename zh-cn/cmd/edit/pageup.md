# 上一页命令

## 摘要

移动光标到上一页。

## 说明

把光标向上移一页。光标会向上移半页，如果在配置属性对话框中的 [**滚动** 页面](../../dlg/properties/scroll/index) 上的 **滚动半页** 复选框被勾选。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **垂直移动光标**
\> **上一页**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: PAGE UP

## 插件命令ID

```
EEID_PAGEUP (4162)```

## 宏

### \[JavaScript\]

```
document.selection.PageUp(false,1);
```

### \[VBScript\]

```
document.selection.PageUp false,1
```
