# EP\_SET\_UNINSTALL

Uninstalls the plug-in.

EP\_SET\_UNINSTALL

hwnd = hwndParent;

wParam = (WPARAM) (LPTSTR) pszUninstallCommand;

lParam = (LPARAM) (LPTSTR) pszUninstallParam;

## Parameters

_hwndParent_

> The window handle of the Plug-ins Settings dialog box.

_pszUninstallCommand_

> Specifies the command to run when the return value is UNINSTALL\_RUN\_COMMAND.

_pszUninstallParam_

> Specifies the parameter for the command to run when the return value is UNINSTALL\_RUN\_COMMAND.

## Return Values

> The return value is one of following values.
>
> |     |     |
> | --- | --- |
> | UNINSTALL\_FALSE | Does not uninstall. |
> | UNINSTALL\_SIMPLE\_DELETE | Simply removes the plug-in DLL file. |
> | UNINSTALL\_RUN\_COMMAND | Runs the specified command. |
>
> If the return value is TRUE, the plug-in will be uninstalled. If the return
> value is FALSE, the plug-in will not be uninstalled.

## Version

> Supported on Version 3.00 or later. However, the return value UNINSTALL\_RUN\_COMMAND and pszUninstallCommand parameter and pszUninstallParam parameter are supported on Version 6.00 or later.
