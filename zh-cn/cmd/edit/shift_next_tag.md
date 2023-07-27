# 扩展选区到配对的标记命令

## 摘要

把选区扩展到配对的标记。

## 说明

在一个XML或XHTML文档中，当光标位于一个开始/结束标记处，这个命令会把选区扩展到相对应的结束/开始标记处。

## 运行方法

- 默认菜单:搜索 \>选择当前标签
- [所有命令](../tools/all_commands):编辑 \>扩展选区
\>扩展选区至匹配的标签
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+.

## 插件命令ID

```
EEID_SHIFT_NEXT_TAG (4602)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4602);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4602
```
