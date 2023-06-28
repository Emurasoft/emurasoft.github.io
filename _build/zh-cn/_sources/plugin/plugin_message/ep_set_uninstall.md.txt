# EP\_SET\_UNINSTALL

卸载插件。

EP\_SET\_UNINSTALL

hwnd = hwndParent;

wParam = (WPARAM) (LPTSTR) pszUninstallCommand;

lParam = (LPARAM) (LPTSTR) pszUninstallParam;

## 参数

_hwndParent_

> 插件设定对话框的窗口处理。

_pszUninstallCommand_

> 指定要运行的指令当返回值是 UNINSTALL\_RUN\_COMMAND 时。

_pszUninstallParam_

> 指定要运行的命令的参数当返回值是 UNINSTALL\_RUN\_COMMAND 时。

## 返回值

> 返回值可以是下列值之一。
>
> |     |     |
> | --- | --- |
> | UNINSTALL\_FALSE | 不卸载。 |
> | UNINSTALL\_SIMPLE\_DELETE | 只移除 DLL 插件文件。 |
> | UNINSTALL\_RUN\_COMMAND | 运行指定的命令。 |
>
> 如果返回值是 TRUE，插件将被卸载。如果返回值是 FALSE，插件将不会被卸载。

## 版本

> 支持 Version 3.00 或之后的版本。但是，返回值 UNINSTALL\_RUN\_COMMAND 以及 pszUninstallCommand 参数还有 pszUninstallParam 参数支持 Version 6.00 或之后的版本。