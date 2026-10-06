# 比较命令

## 摘要

不指定参数比较最后访问的两个文档。

## 说明

不指定参数，直接比较两个最近访问的文档。EmEditor 将会出现提示如果两个文件的编码不一致，但还是会继续进行比较。

处于快速查看模式的文档在找到文档的所有行之后也可以进行比较。当文档处于快速查看模式时，[**忽略注释**](ignore_comment)、[**复制到另一窗格**](copy_to_other)、[**全部复制到另一窗格**](copy_all_to_other) 和 [**为有改动的行设置书签**](compare_bookmark) 命令不可用。

## 运行方法

- 默认菜单: **比较** \> **直接比较**
- [所有命令](../tools/all_commands): **比较** \> **比较**
- 工具栏:  ![](../../images/compare24x16.png)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_COMPARE_DIRECT (4492)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4492);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4492
```
