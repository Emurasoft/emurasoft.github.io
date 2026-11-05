# EE\_OUTPUT\_STRING

Appends a string to the Output Bar. You can send this
message explicitly or use the [Editor\_OutputString](../macro/editor_outputstring) inline function.

```
EE_OUTPUT_STRING
wParam = nFlags;
lParam = (LPARAM) (LPCWSTR) szString;
```

## Parameters

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_OPEN\_OUTPUT | Opens the Output Bar. |
| FLAG\_CLOSE\_OUTPUT | Closes the Output Bar. |
| FLAG\_FOCUS\_OUTPUT | Sets the keyboard focus to the Output Bar. |
| FLAG\_CLEAR\_OUTPUT | Clears the contents of the Output Bar. |

_szString_

Specifies the string to be appended.

## Return Values

If the message succeeds, the return value is nonzero. If the message fails,
the return value is zero.

## Version

Supported on EmEditor Version 7.00 or later.
