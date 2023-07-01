# EE\_EXEC\_PLUGIN

執行一個指定的外掛程式。你可以明確地發送該消息或用 [Editor\_ExecPlugin](../macro/editor_execplugin) 內嵌函式。.

EE\_EXEC\_PLUGIN

wParam = (WPARAM) (EXEC\_PLUGIN\_INFO\*) pPluginInfo;

lParam = 0;

## 參數

_pPluginInfo_

> 指向 [**EXEC\_PLUGIN\_INFO** 結構](../structure/exec_plugin_info)。

## 返回值

> 如果發生錯誤，返回值是負值。如果指定的是 PLUGIN\_FLAG\_EXEC\_COMMAND，返回值為 0。如果指定 PLUGIN\_FLAG\_USER\_MSG，返回值的含義取決于外掛程式。如果指定 PLUGIN\_FLAG\_QUERY\_STATUS，返回值則會是下列值的組合。
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | 啟用外掛程式。 |
> | STATUS\_LATCHED | 勾選外掛程式。 |

## 版本

> 支持 EmEditor Professional Version 15.5 或之後的版本。
