# 扩展选区到逻辑行行末命令

## 摘要

把选区扩展到当前逻辑行的行末。

## 说明

把选区扩展到当前逻辑行的行末。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>扩展选区
\>扩展选区到逻辑行行末
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+SHIFT+END

## 插件命令ID

```
EEID_SHIFT_LOGICAL_END (4183)```

## 宏

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
```

### \[VBScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
```
