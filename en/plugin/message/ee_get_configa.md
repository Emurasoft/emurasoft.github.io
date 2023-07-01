# EE\_GET\_CONFIGA

Retrieves the selected configuration name by an ANSI string. You can send
this message explicitly or use the
[Editor\_GetConfigA](../macro/editor_getconfiga) inline function.

EE\_GET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPSTR) szConfigName;

## Parameters

_szConfigName_

> Specifies a buffer that will receive the configuration name. The buffer
> size must be at least MAX\_CONFIG\_NAME bytes.

## Return Values

> The return value is not used.
