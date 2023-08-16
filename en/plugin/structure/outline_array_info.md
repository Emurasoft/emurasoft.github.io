# OUTLINE\_ARRAY\_INFO

Used by
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray)
inline function ( [EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) message).

```
typedef struct _OUTLINE_ARRAY_INFO {
	int nVersion;
	UINT nFlags;
	INT_PTR nStartLine;
	INT_PTR nCount;
	BYTE* pLevelData;
} SET_INFO;
```

## Fields

_nVersion_

Reserved. Must be 1.

_nFlags_

Reserved. Must be 0.

_nCount_

Specifies the number of multiple lines.

_pLevelData_

Specifies an array of BYTE that specifies the outline levels.

## Version

Supported in Version 13 or later.
