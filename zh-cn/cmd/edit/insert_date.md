# 时间和日期命令

## 摘要

插入时间与日期。

## 说明

在光标位置处插入当前时间和日期。这个命令会先插入时间，接着一个空格，跟着是日期。插入的时间与日期的格式可以在 Windows 系统上配置。在控制面板 中选择区域和语言选项，然后选择日期和时间。

## 运行方法

- 默认菜单:插入 \>时间和日期
- [所有命令](../tools/all_commands):插入 \>时间和日期
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_INSERT_DATE (4137)```

## 宏

### \[JavaScript\]

```
document.selection.InsertDate(eeDateTimeDate);
```

### \[VBScript\]

```
document.selection.InsertDate eeDateTimeDate
```
