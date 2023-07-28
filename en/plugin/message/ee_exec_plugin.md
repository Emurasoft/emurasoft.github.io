# EE\_EXEC\_PLUGIN

Executes a specified plug-in. You can send this message explicitly or use
the [Editor\_ExecPlugin](../macro/editor_execplugin) inline function.

EE\_EXEC\_PLUGIN

wParam = (WPARAM) (EXEC\_PLUGIN\_INFO\*) pPluginInfo;

lParam = 0;

## Parameters

_pPluginInfo_

Pointer to the [**EXEC\_PLUGIN\_INFO** structure](../structure/exec_plugin_info).

## Return Value

The return value is a negative value If an error occurs. Otherwise, if PLUGIN\_FLAG\_EXEC\_COMMAND is specified, the return value is 0. If PLUGIN\_FLAG\_USER\_MSG is specified, the meaning of the return values depends on each plug-in. If PLUGIN\_FLAG\_QUERY\_STATUS is specified, the method returns a combination of the following values.

|     |     |
| --- | --- |
| STATUS\_ENABLED | The plug-in is enabled. |
| STATUS\_LATCHED | The plug-in is checked. |

## Version

Supported on EmEditor Professional Version 15.5 or later.
