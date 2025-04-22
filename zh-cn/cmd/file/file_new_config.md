# 新建配置列表命令

## 摘要

用一个指定配置(多个项目)创建一个新文件。

## 说明

这个命令由多个文件项目组成。你可以从预先定义的配置中选取。这个命令会用指定的配置创建一个新文件。你可以编辑，删除，或在 [**定义配置** 对话框](../../dlg/configurations/index) 中添加配置。

## 运行方法

- 默认菜单: **文件** \> **新建** \> **(配置名称)**
- [所有命令](../tools/all_commands): **文件** \> **新建 \> (配置名称)**
- 工具栏: ![](../../images/filenew.png) (点击向下箭头) \+ (配置名称)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_FILE_NEW_CONFIG 到 ID_FILE_NEW_CONFIG + 255 (从 7168
```
到 7168 + 255)

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(7168 + i);  // i 是一个从 0 到 255 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 7168 + i  ' i 是一个从 0 到 255 的整数
```
