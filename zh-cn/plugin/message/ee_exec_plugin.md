# EE\_EXEC\_PLUGIN

执行一个指定的插件。你可以明确地发送该消息或用 [Editor\_ExecPlugin](../macro/editor_execplugin) 内联函数。.

EE\_EXEC\_PLUGIN

wParam = (WPARAM) (EXEC\_PLUGIN\_INFO\*) pPluginInfo;

lParam = 0;

## 参数

_pPluginInfo_

指向 [**EXEC\_PLUGIN\_INFO** 结构](../structure/exec_plugin_info)。

## 返回值

如果发生错误，返回值是负值。如果指定的是 PLUGIN\_FLAG\_EXEC\_COMMAND，返回值为 0。如果指定 PLUGIN\_FLAG\_USER\_MSG，返回值的含义取决于插件。如果指定 PLUGIN\_FLAG\_QUERY\_STATUS，返回值则会是下列值的组合。

|     |     |
| --- | --- |
| STATUS\_ENABLED | 启用插件。 |
| STATUS\_LATCHED | 勾选插件。 |

## 版本

支持 EmEditor Professional Version 15.5 或之后的版本。
