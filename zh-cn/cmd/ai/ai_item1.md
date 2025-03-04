# AI 提示命令

## 摘要

询问指定的 AI 提示(多个项目)。

## 说明

此命令包含多个菜单项。您可以运行此命令来询问在 **自定义** 对话框的 [**AI 提示** 页面](../../dlg/customize/ai_list/index) 中定义的 AI 提示。当您运行此命令时，它会使用您指定的 AI 提示向 AI 提问。

## 运行方法

- 默认菜单: **AI** \> **(AI 提示)**
- [所有命令](../tools/all_commands): **AI** \> **(AI 提示)**
- 工具栏: AI 工具栏上的每个按钮
- 状态栏: 无
- 默认快捷键: 无

## 插件命令 ID

```
From EEID_AI_ITEM1 through EEID_AI_ITEM1 + 1023 (从 29184 到 29184 + 1023)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(29184+i);  // i 是一个从 0 到 1023 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 29184+i  ' i 是一个从 0 到 1023 的整数
```