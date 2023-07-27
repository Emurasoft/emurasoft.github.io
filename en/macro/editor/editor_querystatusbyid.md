# QueryStatusByID Method (Editor Object)

Retrieves the current status of the specified command, whether it is enabled
and checked.

## 

### \[JavaScript\]

```
nStatus = editor.QueryStatusByID( nID );
```

### \[VBScript\]

```
nStatus = editor.QueryStatusByID( nID )
```

## Parameters

_nID_

Specifies an integer indicating the Command ID to execute. See the
[Command Reference](../../cmd/index) for the list of available
commands. Not all commands may be available or supported.

## Return Values

Returns a combination of the following values.

|     |     |
| --- | --- |
| eeStatusEnabled | The command is enabled. |
| eeStatusLatched | The command is checked. |

## Version

Supported on EmEditor Professional Version 4.00 or later.
