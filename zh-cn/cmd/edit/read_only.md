# 只读命令

## 摘要

切换当前文件的只读状态。

## 说明

启用或禁用文件的只读状态。

在快速查看模式下，打开只读也会关闭编辑，关闭只读则允许编辑。如果文档有未保存的编辑内容，EmEditor 会询问是否保存这些编辑内容。详细信息请参见[以快速查看模式打开和编辑超大文件](../../howto/file/file_fast_view)。

## 运行方法

- 默认菜单: **编辑** \> **只读**
- [所有命令](../tools/all_commands): **编辑** \> **高级**
\> **只读**
- 工具栏: 无
- 状态栏: 双击 **“只读”**
- 默认快捷键: 无

## 插件命令ID

```
EEID_READ_ONLY (4113)```

## 宏

### \[JavaScript\]

```
document.ReadOnly=true;
或
document.ReadOnly=false;
```

### \[VBScript\]

```
document.ReadOnly=true
或
document.ReadOnly=false
```
