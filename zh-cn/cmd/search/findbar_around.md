# 循环 (查找工具栏) 命令

## 摘要

切换工具栏上「循环」按钮的状态。

## 说明

切换工具栏上「循环」按钮的状态。切换此命令后，用 **查找下一个** 或 **查找上一个** 期间到达文档的结尾或开头处时，EmEditor 将移动到文档的开头或结尾处以继续搜索。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **搜索**
\> **查找工具栏** \> **循环**
- 工具栏: ![](../../images/find_around.png) (查找工具栏)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FINDBAR_AROUND (4577)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4577);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4577
```
