# 大写命令

## 摘要

把选定文本全部转换为大写字符。

## 说明

把选定文本全部转换为大写字符。例如，a 会变成 A, ä 会变成 Ä，还有 λ 会变成 Λ.

## 运行方法

- 默认菜单: **转换** \> **大写**
- [所有命令](../tools/all_commands): **转换** \> **大写**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+U

## 插件命令ID

```
EEID_MAKE_UPPER (4149)```

## 宏

### \[JavaScript\]

```
document.selection.ChangeCase(eeCaseUpperCase);
```

### \[VBScript\]

```
document.selection.ChangeCase eeCaseUpperCase
```
