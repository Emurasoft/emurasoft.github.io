# EE\_SET\_CONFIGA

Changes to a configuration specified by an ANSI string. You can send this
message explicitly or use the
[Editor\_SetConfigA](../macro/editor_setconfiga)
inline function.

EE\_SET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## Parameters

_szConfigName_

> Specifies a configuration by an ANSI string.

## Return Values

> The return value is not used.