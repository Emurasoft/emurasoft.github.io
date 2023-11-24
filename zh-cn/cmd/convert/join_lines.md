# 连接行命令

## 摘要

通过移除换行符和在行尾插入空格来连接行。

## 说明

删除选区中换行点处的换行符。与 [**删除换行符** 命令](delete_cr_wrap) 相似，但是该命令会在每一行的换行点处插入空格。

## 运行方法

- 默认菜单: **转换** \> **连接行**
- [所有命令](../tools/all_commands): **转换** \> **连接行**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_JOIN_LINES (4378)```

## 宏

### \[JavaScript\]

```
document.selection.Format(eeFormatJoinLines);
```

### \[VBScript\]

```
document.selection.Format eeFormatJoinLines
```
