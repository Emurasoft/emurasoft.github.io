# 查找上一个命令

## 摘要

查找上一个匹配。

## 说明

用同样的参数查找与之前搜索过的字符串相同的上一个匹配。

## 运行方法

- 默认菜单: **搜索** \> **上一个**
- [所有命令](../tools/all_commands): **搜索**
\> **上一个**
- 工具栏:
![](../../images/editrepeatback.png)
- 状态栏: 无
- 默认快捷键: SHIFT+F3

## 插件命令ID

```
EEID_EDIT_REPEAT_BACK (4203)
```

## 宏

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatPrevious);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatPrevious
```
