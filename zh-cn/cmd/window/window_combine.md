# 启用标签页命令

## 摘要

启用标签页对窗口进行合并或禁用标签页分割所有窗口。

## 说明

启用标签页当标签页被禁用时，或者禁用标签页当标签页被启用时。当标签页被启用，所有当前打开的文档会被显示在窗口上方的的标签菜单上。只有一个 EmEditor 图标会被显示在 Windows 任务栏中。

## 运行方法

- 默认菜单: **窗口** \> **启用标签页**
- [所有命令](../tools/all_commands): **窗口**
\> **启用标签页** \> **启用标签页**
- 工具栏: ![](../../images/windowcombine.png)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令 ID

- EEID\_WINDOW\_COMBINE (4342)

## 宏

### \[JavaScript\]

```
editor.EnableTab = !editor.EnableTab;
```

### \[VBScript\]

```
editor.EnableTab = Not editor.EnableTab
```
