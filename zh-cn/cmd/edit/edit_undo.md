# 撤消命令

## 摘要

撤消上一次的操作。

## 说明

撤消上一次的操作。如果你重复这个指令，你能撤消连续的前几次操作。如果 [自定义 对话框](../../dlg/customize/index) 中 [编辑 页面](../../dlg/customize/edit/index) 是上
“逐格撤消” 复选框被勾选，一个字符串的插入会被一个字符一个字符的撤消。

## 运行方法

- 默认菜单:编辑 \>撤消
- [所有命令](../tools/all_commands):编辑 \>撤消
- 工具栏: ![](../../images/editundo.gif)
- 状态栏: 无
- 默认快捷键: CTRL+Z 或 ALT+BACKSPACE

## 插件命令ID

```
EEID_EDIT_UNDO (4124)```

## 宏

### \[JavaScript\]

```
document.Undo();
```

### \[VBScript\]

```
document.Undo
```
