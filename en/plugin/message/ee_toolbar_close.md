# EE\_TOOLBAR\_CLOSE

Closes a custom toolbar. You can send this message explicitly or
by using the [Editor\_ToolbarClose](../macro/editor_toolbarclose) inline function.

```
EE_TOOLBAR_CLOSE
(UINT)wParam = nToolbarID
```

## Parameters

_nToolbarID_

Specifies the toolbar to close. This is the return value from the EE\_TOOLBAR\_OPEN message.

## Return Values

If the message succeeds and the toolbar state has been changed, the return value is TRUE. If the message fails or the toolbar state has not been changed, the return value is FALSE.

## Version

Supported on EmEditor Professional Version 7.00 or later.
