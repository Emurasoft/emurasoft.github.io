# 保存为不带签名的 UTF-8 命令

## 摘要

用不带签名的 Unicode (UTF-8) 编码保存当前文件。

## 说明

这个命令会用不带签名的 Unicode (UTF-8)编码保存当前文件，除非文档还未被命名。如果文档无标题，会出现一个另存为 对话框，让你输入一个文件名来保存文件。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):文件 \>保存
\>以指定编码保存 \>保存为不带签名的 UTF-8
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SAVE_UTF8_NOSIGN (4488)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4488);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4488
```
