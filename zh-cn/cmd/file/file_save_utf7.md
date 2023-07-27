# 保存为 UTF-7 命令

## 摘要

用 Unicode(UTF-7) 编码保存当前文件。

## 说明

这个命令会用 Unicode(UTF-7) 编码保存当前文件，除非文档还未被命名。如果文档无标题，会出现一个另存为 对话框，让你输入一个文件名来保存文件。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):文件 \>保存
\>以指定编码保存 \>保存为 UTF-7
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_SAVE_UTF7 (4256)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4256);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4256
```
