# 当前文档中的下一个书签命令

## 摘要

转到当前文档中的下一个书签。

## 说明

把光标移动到当前文档中的下一个书签。如果在当前文档中不存在任何书签的话，该命令将不会移动光标。

## 运行方法

- 默认菜单: **书签** \> **下一个书签**
- [所有命令](../tools/all_commands): **书签** \> **下一个书签**
- 工具栏: ![](../../images/bookmarknextwithin..png)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_BOOKMARK_NEXT_WITHIN (4351)
```

## 宏

### \[JavaScript\]

```
document.selection.NextBookmark();
```

### \[VBScript\]

```
document.selection.NextBookmark
```
