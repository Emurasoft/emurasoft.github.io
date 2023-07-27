# 按激活顺序排列命令

## 摘要

按激活顺序排列标签页。

## 说明

按激活顺序排列标签页（最近激活的文档出现在最左边）。如果勾选了 [自动排列 命令](auto_sort)，每当一个文件被打开或一个文档被激活时，标签页就会按这个命令自动排列。如果 [自动排列 命令](auto_sort) 没有被勾选的话，这个命令只会执行一次。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):查看 \>标签排列方式
\>可用
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SORT_ZORDER (4401)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4401);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4401
```
