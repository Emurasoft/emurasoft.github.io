# 插入代码片段命令

## 摘要

在当前光标位置插入指定的代码片段（多项）。

## 说明

该命令由多个菜单项组成，允许您选择一个代码片段插入到光标位置。

## 运行方法

- 默认菜单：**插入** > **（插入代码片段）**
- [所有命令](../tools/all_commands)：**插入** > **代码片段** > **（插入代码片段）**
- 工具栏：无
- 状态栏：无
- 默认快捷键：无

## 插件命令 ID

```
从 EEID_INSERT_SNIPPET1 到 EEID_INSERT_SNIPPET1 + 1023（从 30208 到 30208 + 1023）
```

## 宏

## [JavaScript]

```
editor.ExecuteCommandByID(30208 + i); // i 是一个从 0 到 1023 的整数
```

## [VBScript]

```
editor.ExecuteCommandByID 30208 + i   ' i 是一个从 0 到 1023 的整数
```