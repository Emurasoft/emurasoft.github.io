# 字典命令

## 摘要

选择该字典来检查拼写（多个项目）。

## 说明

选择该字典来检查拼写。EmEditor安装程序已含有一个美式英语词典。额外的字典可以在 **[OpenOffice.org wiki](https://wiki.openoffice.org/wiki/Dictionaries)** 中下载。要添加一个字典，复制 **\*.dic** 和 **\*.aff** 文件到 **Dictionaries（字典）**，即 EmEditor 安装文件夹的子文件夹中 (通常是在 C:\\Program Files\\EmEditor\\Dictionaries 中)。

## 运行方法

- 默认菜单: **编辑** \> **拼写检查** \> **字典** \> **(字典)**
- [所有命令](../tools/all_commands): **编辑** \> **拼写检查** \> **字典** \> **(字典)**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_SELECT_DICTIONARY 到 EEID_SELECT_DICTIONARY + 255 (从 22016 到 22016 + 255)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(22016 + i);  // i 是一个从 0 到 255 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22016 + i  ' i 是一个从 0 到 255 的整数
```
