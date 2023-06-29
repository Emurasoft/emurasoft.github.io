# EE\_LOAD\_CONFIGA

Reloads a configuration of which name is specified by an ANSI string. You can
send this message explicitly or use the
[Editor\_LoadConfigA](../macro/editor_loadconfiga)
inline function.

EE\_LOAD\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## Parameters

_szConfigName_

> Specifies the name of a configuration to be reloaded.

## Return Values

> The return value is not used.