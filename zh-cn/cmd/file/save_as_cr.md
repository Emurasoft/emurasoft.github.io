# 保存换行为 CR 命令

## 摘要

只以 CR 方式保存换行。

## 说明

这个命令会在保存文档之前把所有新行转换成仅 CR 的换行方式（Macintosh）。如果文档没有标题，则会出现一个另存为 对话框，让你能输入一个文件名来保存文件。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):文件 \>保存
\>使用不同的换行符保存 \>保存为 CR
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SAVE_AS_CR (4106)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4106);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4106
```
