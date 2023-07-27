# EE\_SET\_CONFIGW

Changes to a configuration specified by a Unicode string. You can send this
message explicitly or use the
[Editor\_SetConfigW](../macro/editor_setconfigw)
inline function.

EE\_SET\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## Parameters

_szConfigName_

Specifies a configuration by a Unicode string.

## Return Values

The return value is not used.
