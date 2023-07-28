# 非制表位化整个文档命令

## 摘要

把整个文档中制表符转换为相同的空格。

## 说明

把整个文档中所有行开头出的制表符转换为空格。一个制表符所代表的空格数可以在 [**“制表符/缩进”** 对话框](../../dlg/properties/general/indent/index) 中设置。在选择整个文档后，该命令与 [**非制表位化** 命令](untabify) 相同，但该命令不会延伸到选取区域以外的地方。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **高级** \> **将文档中的制表符转换为空格**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_TAB_TO_SPACE (4253)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4253);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4253
```
