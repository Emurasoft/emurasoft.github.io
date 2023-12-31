# 制表位化整个文档命令

## 摘要

把整个文档中的相同的空格转换为制表符。

## 说明

把整个文档中的相同的空格转换为制表符。转换的空格数与一个制表符所代表的空格数相同。一个制表符所代表的空格数可以在 [**“制表符/缩进”** 对话框](../../dlg/properties/general/indent/index) 中设置。在选择整个文档后，该命令与 [**制表位化** 命令](../convert/tabify) 相同，但该命令不会延伸到选取区域以外的地方。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **高级** \> **将文档中的空格转换为制表符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SPACE_TO_TAB (4355)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4355);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4355
```
