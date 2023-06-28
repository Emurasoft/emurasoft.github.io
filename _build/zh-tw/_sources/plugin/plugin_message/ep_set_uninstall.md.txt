# EP\_SET\_UNINSTALL

卸載外掛程式。

EP\_SET\_UNINSTALL

hwnd = hwndParent;

wParam = (WPARAM) (LPTSTR) pszUninstallCommand;

lParam = (LPARAM) (LPTSTR) pszUninstallParam;

## 參數

_hwndParent_

> 外掛程式設定對話方塊的視窗處理。

_pszUninstallCommand_

> 指定要運行的指令當返回值是 UNINSTALL\_RUN\_COMMAND 時。

_pszUninstallParam_

> 指定要運行的命令的參數當返回值是 UNINSTALL\_RUN\_COMMAND 時。

## 返回值

> 返回值可以是下列值之一。
>
> |     |     |
> | --- | --- |
> | UNINSTALL\_FALSE | 不卸載。 |
> | UNINSTALL\_SIMPLE\_DELETE | 只移除 DLL 外掛程式檔案。 |
> | UNINSTALL\_RUN\_COMMAND | 運行指定的命令。 |
>
> 如果返回值是 TRUE，外掛程式將被卸載。如果返回值是 FALSE，外掛程式將不會被卸載。

## 版本

> 支持 Version 3.00 或之後的版本。但是，返回值 UNINSTALL\_RUN\_COMMAND 以及 pszUninstallCommand 參數還有 pszUninstallParam 參數支持 Version 6.00 或之後的版本。