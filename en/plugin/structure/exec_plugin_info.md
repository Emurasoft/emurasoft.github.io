# EXEC\_PLUGIN\_INFO

Used by [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) message.

```
typedef struct _EXEC_PLUGIN_INFO {
	UINT cbSize;
	LONG nFlags;
	LPCWSTR pszName;
	WPARAM wParam;
	LPARAM lParam;
	LONG_PTR nResult;
} EXEC_PLUGIN_INFO;
```

## Fields

_cbSize_

Specifies the size of this structure, sizeof( EE\_PLUGIN\_INFO ).

_nFlags_

Specifies a combination of the following values. eePluginExecuteCommand, eePluginUserMessage, and eePluginQueryStatus must be mutually exclusively specified.

|     |     |
| --- | --- |
| PLUGIN\_FLAG\_EXEC\_COMMAND | Runs the plug-in as if a user selected the plug-in command. The wParam and lParam parameters are ignored when this is specified. |
| PLUGIN\_FLAG\_USER\_MSG | Sends a message to the plug-in using the wParam and lParam parameters. |
| PLUGIN\_FLAG\_QUERY\_STATUS | Retrieves the plug-in status. The wParam and lParam parameters are ignored when this is specified. |
| PLUGIN\_FLAG\_ABSOLUTE\_PATH | The pszName contains the full path to the file. If this flag is not specified, the plug-in must exist in the default plug-in folder, which is PlugIns subfolder of the EmEditor install folder. |

_pszName_

Specifies the plug-in file name.

_wParam_

Specifies the first parameter to send to the plug-in. The meaning of the parameter depends on each plug-in.

_lParam_

Specifies the second parameter to send to the plug-in. The meaning of the parameter depends on each plug-in.

## Version

Supported on EmEditor Professional Version 15.5 or later.
