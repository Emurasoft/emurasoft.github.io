# 删除到行末命令

## 摘要

从光标位置删除到行末。

## 说明

从光标位置删除文本，直到光标所在的逻辑行的行末。

## 运行方法

- 默认菜单:编辑 \>高级 \>删除到行末
- [所有命令](../tools/all_commands):编辑 \>删除
\>删除到行末
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_DELETE_RIGHT_LINE (4191)```

## 宏

## \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
document.selection.Delete(1);
```

## \[VBScript\]

```
document.selection.EndOfLine true,eeLineLogical
document.selection.Delete 1
```
