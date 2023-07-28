# 拼写建议命令

## 摘要

选择正确的拼写建议（多个项目）。

## 说明

选择正确的拼写建议，并用选取的建议取代拼写不正确的字词。(该命令不会取代整个文档中拼写错误的单词)。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **拼写检查** \> **(拼写建议)**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_SPELL_SUGGEST 到 EEID_SPELL_SUGGEST + 31 (从 8768 到 8768 + 31)```

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(8768 + i);  // i 是一个从 0 到 31 的整数
```

## \[VBScript\]

```
editor.ExecuteCommandByID 8768 + i  ' i 是一个从 0 到 31 的整数
```
