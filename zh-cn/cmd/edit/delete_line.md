# 删除行命令

## 摘要

删除选取的行或当前行。

## 说明

删除选取的行或光标处的一逻辑行。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>删除
\>删除行
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+L

## 插件命令ID

```
EEID_DELETE_LINE (4190)```

## 宏

### \[JavaScript\]

```
document.selection.SelectLine();
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.SelectLine
document.selection.Delete 1
```
