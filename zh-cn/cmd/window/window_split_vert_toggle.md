# 切换垂直分割命令

## 摘要

切换垂直窗口分割。

## 说明

如果当前窗口被水平分割或完全不分割，这个命令将分割把当前窗口分割成垂直窗格，并且会在窗口中心固定分割位置。如果当前窗口已经被垂直分割了，这个命令则会从当前窗口中移除垂直分割。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **窗口**
\> **分割** \> **切换垂直窗口分割**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令 ID

- EEID\_WINDOW\_SPLIT\_VERT\_TOGGLE (4386)

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4386);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4386
```
