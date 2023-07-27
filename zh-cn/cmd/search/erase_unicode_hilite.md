# 取消 Unicode 高亮命令

## 摘要

取消高亮显示无法转换为要保存的编码的 Unicode 字符。

## 说明

为被搜索的无法转换为要保存的编码 Unicode 字符重设高亮。这个命令还能重置用 [查找下一个 Unicode 字符 命令](find_next_unicode) 或 [查找上一个 Unicode 字符 命令](find_prev_unicode) 设定的要保存的编码。

## 运行方法

- 默认菜单:搜索 \>取消 Unicode 高亮
- [所有命令](../tools/all_commands):搜索 \>Unicode \>取消 Unicode 高亮
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+F9

## 插件命令ID

```
EEID_ERASE_UNICODE_HILITE (4377)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4377);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4377
```
