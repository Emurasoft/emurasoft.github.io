# ExecutePlugin Method (Editor Object)

Executes a specified plug-in.

## 

### \[JavaScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam );
```

### \[VBScript\]

```
nResult = editor.ExecutePlugin( strPluginFileName, nFlags, nParam, strParam )
```

## Parameters

_strPluginFileName_

Specifies the plug-in file name.

_nFlags_

Specifies a combination of the following values. eePluginExecuteCommand, eePluginUserMessage, and eePluginQueryStatus must be mutually exclusively specified.

|     |     |
| --- | --- |
| eePluginExecuteCommand | Runs the plug-in as if a user selected the plug-in command. The nParam and strParam parameters are ignored when this is specified. |
| eePluginUserMessage | Sends a message to the plug-in using the nParam and strParam parameters. |
| eePluginQueryStatus | Retrieves the plug-in status. The nParam and strParam parameters are ignored when this is specified. |
| eePluginAbsolutePath | The strPluginFileName contains the full path to the file. If this flag is not specified, the plug-in must exist in the default plug-in folder, which is PlugIns subfolder of the EmEditor install folder. |

_nParam_

Specifies the integer parameter to send to the plug-in. The meaning of the parameter depends on each plug-in. If this is omitted, 0 is specified.

_strParam_

Specifies the string parameter to send to the plug-in. The meaning of the parameter depends on each plug-in. If this is omitted, an empty string is specified.

## Return Values

The return value is a negative value If an error occurs. Otherwise, if eePluginExecuteCommand is specified, the return value is 0. If eePluginUserMessage is specified, the meaning of the return values depends on each plug-in. If eePluginQueryStatus is specified, the method returns a combination of the following values.

|     |     |
| --- | --- |
| eeStatusEnabled | The plug-in is enabled. |
| eeStatusLatched | The plug-in is checked. |

## Examples

### \[JavaScript\]

```
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0" );
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 1, "General\\\Date");
editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 2, "/General/Date" );
```

### \[VBScript\]

```
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 1, "General" & Chr(92) & "Date"
editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 2, "/General/Date"
```

## Version

Supported on EmEditor Professional Version 15.5 or later.
