# \#status directive (Script Directives)

Specifies the status (whether the macro is enabled and whether it is checked) of the current macro which should mimic the command specified by the ID. The Macros menu and Macros toolbar updates the macro status according to this specified command status. This directive must be specified at the first lines of the script above the main code.

#status = _id_

## Parameters

_id_

Specifies the integer value of the command ID that is used to query the status. This value is equivalent to the _nID_ parameter of the [QueryStatusByID method](../editor/editor_querystatusbyid).

## Examples

This macro mimics the Auto Copy command (ID = 3979). The macro menu and toolbar button is checked when the Auto Copy feature is on. The macro menu and toolbar button is not checked when the Auto Copy feature is off.

### \[JavaScript\]

```
```

#status = 3979

editor.ExecuteCommandByID(3979);   // 3979 = EEID\_AUTO\_COPY

## 

### \[VBScript\]

```
```

#status = 3979

editor.ExecuteCommandByID 3979   ' 3979 = EEID\_AUTO\_COPY

## Version

Supported on EmEditor Professional Version 16.4 or later.
