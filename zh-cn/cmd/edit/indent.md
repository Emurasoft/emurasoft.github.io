# 增加行缩进命令

## 摘要

增加选定区域的行缩进。

## 说明

在选定区域内插入一个tab字符到每行的开头。如果多行被选择了，这个命令等同于 [制表符或增加行缩进 命令](tab)。

## 运行方法

- 默认菜单:转换 \>增加行缩进
- [所有命令](../tools/all_commands):转换 \>增加行缩进
- 工具栏: ![](../../images/indent.gif)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_INDENT (4358)```

## 宏

### \[JavaScript\]

```
document.selection.Indent();
```

### \[VBScript\]

```
document.selection.Indent
```
