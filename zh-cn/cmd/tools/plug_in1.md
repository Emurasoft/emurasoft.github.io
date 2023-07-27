# 插件列表命令

## 摘要

运行一个指定的插件（多个项目）。

## 说明

这个命令由多个菜单项目组成。该命令会执行指定的插件。可用的插件可以在 [自定义插件 对话框](../../dlg/plugins/index) 中定义。

## 运行方法

- 默认菜单:插件 \> （插件名称）
- [所有命令](all_commands):插件 \> （插件名称）
- 工具栏: 插件工具栏上的按钮
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
From EEID_PLUG_IN1 through EEID_PLUG_IN1 + 255 （从 5632 到 5632 + 255）```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(5632+i);  // i 是从 0 到 255 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 5632+i  ' i 是从 0 到 255 的整数
```
