# Editor\_ExecPlugin

执行一个指定的插件。你能直接用该内联函数或明确地发送 [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) 消息。

HRESULT Editor\_ExecPlugin( HWND hwnd, LPCWSTR pszName, LONG nFlags, WPARAM wParam, LPARAM lParam, LONG\_PTR\* pnResult );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszName_

> 指定插件文件名。

_nFlags_

> 指定一个下列值的组合。PLUGIN\_FLAG\_EXEC\_COMMAND，PLUGIN\_FLAG\_USER\_MSG，和 PLUGIN\_FLAG\_QUERY\_STATUS 一定要专门指定。
>
> |     |     |
> | --- | --- |
> | PLUGIN\_FLAG\_EXEC\_COMMAND | 如同选择插件命令一样运行插件。如果指定该值，那么忽略 wParam 和 lParam 参数。 |
> | PLUGIN\_FLAG\_USER\_MSG | 用 wParam 和 lParam 参数发送消息至插件。 |
> | PLUGIN\_FLAG\_QUERY\_STATUS | 检索插件状态。如果指定该值，那么忽略 wParam 和 lParam 参数。 |
> | PLUGIN\_FLAG\_ABSOLUTE\_PATH | pszName 包含文件的完整路径。如果不指定这个标志，插件一定要在默认插件文件夹中，即 EmEditor 安装文件夹中的 PlugIns 子文件夹中。 |

_wParam_

> 指定第一个送至插件的参数。参数的含义取决于插件。

_lParam_

> 指定第二个送至插件的参数。参数的含义取决于插件。

## 返回值

> 如果发生错误，返回值是负值。如果指定的是 PLUGIN\_FLAG\_EXEC\_COMMAND，返回值为 0。如果指定 PLUGIN\_FLAG\_USER\_MSG，返回值的含义取决于插件。如果指定 PLUGIN\_FLAG\_QUERY\_STATUS，返回值则会是下列值的组合。
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | 启用插件。 |
> | STATUS\_LATCHED | 勾选插件。 |

## 版本

> 支持 EmEditor Professional Version 15.5 或之后的版本。