# EE\_GET\_CONFIGW

Retrieves the selected configuration name by a Unicode string. You can send
this message explicitly or use the [Editor\_DocGetConfigW](../macro/editor_docgetconfigw) inline function or the
[Editor\_GetConfigW](../macro/editor_getconfigw)
inline function.

```
EE_GET_CONFIGW
wParam = MAKEWPARAM(0, (iDoc)+1);
lParam = (LPARAM) (LPWSTR) szConfigName;
```

## Parameters

_iDoc_

Specifies the index of the target document. A one-based index should be specified at the higher word of wParam. If 0 is specified at the higher word of wParam, the currently active document will
be targeted.

_szConfigName_

Specifies a buffer that will receive the configuration name. The buffer
size must be at least MAX\_CONFIG\_NAME in words.

## Return Values

The return value is not used.
