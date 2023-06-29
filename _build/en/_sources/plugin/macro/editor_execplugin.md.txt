# Editor\_ExecPlugin

Executes a specified plug-in. You can use this inline function or explicitly send
the [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) message.

HRESULT Editor\_ExecPlugin( HWND hwnd, LPCWSTR pszName, LONG nFlags, WPARAM wParam, LPARAM lParam, LONG\_PTR\* pnResult );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pszName_

> Specifies the plug-in file name.

_nFlags_

> Specifies a combination of the following values. PLUGIN\_FLAG\_EXEC\_COMMAND, PLUGIN\_FLAG\_USER\_MSG, and PLUGIN\_FLAG\_QUERY\_STATUSmust be mutually exclusively specified.
>
> |     |     |
> | --- | --- |
> | PLUGIN\_FLAG\_EXEC\_COMMAND | Runs the plug-in as if a user selected the plug-in command. The wParam and lParam parameters are ignored when this is specified. |
> | PLUGIN\_FLAG\_USER\_MSG | Sends a message to the plug-in using the wParam and lParam parameters. |
> | PLUGIN\_FLAG\_QUERY\_STATUS | Retrieves the plug-in status. The wParam and lParam parameters are ignored when this is specified. |
> | PLUGIN\_FLAG\_ABSOLUTE\_PATH | The pszName contains the full path to the file. If this flag is not specified, the plug-in must exist in the default plug-in folder, which is PlugIns subfolder of the EmEditor install folder. |

_wParam_

> Specifies the first parameter to send to the plug-in. The meaning of the parameter depends on each plug-in.

_lParam_

> Specifies the second parameter to send to the plug-in. The meaning of the parameter depends on each plug-in.

## Return Values

> The return value is a negative value If an error occurs. Otherwise, if PLUGIN\_FLAG\_EXEC\_COMMAND is specified, the return value is 0. If PLUGIN\_FLAG\_USER\_MSG is specified, the meaning of the return values depends on each plug-in. If PLUGIN\_FLAG\_QUERY\_STATUS is specified, the method returns a combination of the following values.
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | The plug-in is enabled. |
> | STATUS\_LATCHED | The plug-in is checked. |

## Version

> Supported on EmEditor Professional Version 15.5 or later.