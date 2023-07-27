# 保存为日文 EUC 命令

## 摘要

用日文 EUC 编码保存当前文件。

## 说明

这个命令会用日文 EUC 编码保存当前文件，除非文档未被命名。如果文档没有标题，会出现一个另存为 对话框，让你能输入一个文件名来保存文件。

这个命令与旧版本的 EmEditor 兼容。你还可以使用 [以指定编码保存（多个项目） 命令](file_save_defined) 来指定日文 EUC。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):文件 \>保存
\>以指定编码保存 \>保存为日文 EUC
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_SAVE_EUC (4104)```

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(4104);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4104
```
