# 要插入的最近使用的文件列表命令

## 摘要

插入一个指定的最近访问的文件在光标位置处（多个项目）。

## 说明

这个命令由多个菜单项目组成，让你能选择一个最近访问的文件在光标位置处插入。所显示的最近访问的文件数
可以在工具 菜单（工具 \>自定义 \>历史记录）下的 [自定义 对话框](../../dlg/customize/index) 中 [历史记录 页面](../../dlg/customize/history/index) 上的最近使用的文件数 文本框中设定。

## 运行方法

- 默认菜单:插入 \>（选择文件名）
- [所有命令](../tools/all_commands):插入 \>（选择文件名）
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_FILE_MRU_INSERT1 到 EEID_FILE_MRU_INSERT1 + 63 (从 4864```
到 4864 + 63)

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4864 + i); // i 是一个从 0 到 63 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4864 + i   ' i 是一个从 0 到 63 的整数
```
