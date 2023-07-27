# 扩展选区到上一页命令

## 摘要

把选区向上扩展一页。

## 说明

把选区向上扩展一页。如果配置属性对话框中的 [滚动 页面](../../dlg/properties/scroll/index) 上的滚动半页 复选框被勾选的话，光标只会移动半页。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>扩展选区
\>扩展选区到上一页
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+PAGE UP

## 插件命令ID

```
EEID_SHIFT_PAGEUP (4178)```

## 宏

### \[JavaScript\]

```
document.selection.PageUp(true,1);
```

### \[VBScript\]

```
document.selection.PageUp true,1
```
