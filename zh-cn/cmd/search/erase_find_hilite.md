# 取消查找高亮命令

## 摘要

清除搜索字符串的高亮。

## 说明

清除在当前文档中所有之前搜索过的字符串的高亮。

## 运行方法

- 默认菜单: **搜索** \> **取消高亮**
- [所有命令](../tools/all_commands): **搜索** \> **查找/替换** \> **取消查找突出显示**
- 工具栏:
![](../../images/erasefindhilite.png)
- 状态栏: 无
- 默认快捷键: ALT+F3

## 插件命令ID

```
EEID_ERASE_FIND_HILITE (4206)
```

## 宏

### \[JavaScript\]

```
document.HighlightFind=false;
```

### \[VBScript\]

```
document.HighlightFind=false
```
