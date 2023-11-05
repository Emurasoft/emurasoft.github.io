# EE\_LOAD\_CONFIGW

Reloads a configuration of which name is specified by a Unicode string. You
can send this message explicitly or use the
[Editor\_LoadConfigW](../macro/editor_loadconfigw)
inline function.

```
EE_LOAD_CONFIGW
wParam = 0;
lParam = (LPARAM) (LPCWSTR) szConfigName;
```

## Parameters

_szConfigName_

Specifies the name of a configuration to be reloaded.

## Return Values

The return value is not used.
