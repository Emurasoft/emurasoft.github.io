# Run Method (Shell Object)

Runs a program in a new process.

## 

### \[JavaScript\]

```
nReturnCode = shell.Run( strCommand, nWindowStyle, bWaitOnReturn, strParameter, strFolder );
```

### \[VBScript\]

```
nReturnCode = shell.Run( strCommand, nWindowStyle, bWaitOnReturn, strParameter, strFolder )
```

## Parameters

_strCommand_

Specifies a command. Usually, this is a full path and name of the program file.

_nWindowStyle_

Specifies an integer value indicating the appearance of the program's window. This parameter can be omitted. This parameter can be one of the following value.

|     |     |
| --- | --- |
| Value | Description |
| 1 | Activates and displays a window. If the window is minimized or maximized, the system restores it to its original size and position. |
| 2 | Activates the window and displays it as a minimized window. |
| 3 | Activates the window and displays it as a maximized window. |
| 4 | Displays a window in its most recent size and position. The active window remains active. |

_bWaitOnReturn_

Specifies a boolean value indicating whether the script should wait for the program to finish executing before continuing to the next statement in your script. This parameter can be omitted.

_strParameter_

Specifies a parameter you want to pass as the command line. This parameter can be omitted.

_strFolder_

Specifies an initial directory. This parameter can be omitted.

## Examples

### \[JavaScript\]

```
nAttr = shell.Run( "C:\\\\Windows\\\\calc.exe", 1 );
```

### \[VBScript\]

```
nAttr = shell.Run( "C:\\Test\\file.txt" )
```

## Return Value

Returns a return code of the program if _bWaitOnReturn_ is true. The return value is not used if _bWaitOnReturn_ is false.

## Version

Supported on EmEditor Professional Version 22.1 or later.
