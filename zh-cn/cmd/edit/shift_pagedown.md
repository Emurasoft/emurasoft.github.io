# 扩展选区到下一页命令

## 摘要

把选区向下扩展一页。

## 说明

把选区向下扩展一页。如果配置属性对话框中的 [滚动 页面](../../dlg/properties/scroll/index) 上的滚动半页 复选框被勾选的话，光标只会移动半页。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>垂直移动光标
\>扩展选区到下一页
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+PAGE DOWN

## 插件命令ID

```
EEID_SHIFT_PAGEDOWN (4179)```

## 宏

## \[JavaScript\]

```
document.selection.PageDown(true,1);
```

## \[VBScript\]

```
document.selection.PageDown true,1
```
