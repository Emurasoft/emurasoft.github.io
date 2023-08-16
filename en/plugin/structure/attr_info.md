# ATTR\_INFO

Used by [EE\_GET\_ATTR](../message/ee_get_attr) message.

```
typedef struct _ATTR_INFO {
	size_t cbSize; // in
	POINT_PTR ptLogical; // in
	UINT nFlags; // in
	UINT nAttr; // out
	WCHAR szConfigScope[MAX_CONFIG_NAME]; // out
	WCHAR szConfigDoc[MAX_CONFIG_NAME]; // out
} ATTR_INFO;
```

## Members

_cbSize_

\[In\] Size of this data structure, in bytes. Set this member to sizeof( ATTR\_INFO ) before sending the [EE\_GET\_ATTR](../message/ee_get_attr) message.

_ptLogical_

\[In\] Specifies the position in the logical coordinate where information should be retrieved.

_nFlags_

\[In\] Specifies a combination of the following values.

|     |     |
| --- | --- |
| AI\_NEED\_CONFIG\_SCOPE | Needs the name of the configuration (scope) at the specified position on the active document. |
| AI\_NEED\_CONFIG\_DOC | Needs the name of the configuration selected for the active document. |
| AI\_NEED\_ATTR\_SUB | Saves the temporary text specified by nID. |
| AI\_NEED\_ALL | Needs all the above information. |

_nAttr_

\[Out\] This member contains one of the following values.

|     |     |
| --- | --- |
| ATTR\_NONE | Normal text. |
| ATTR\_COMMENT | A comment. |
| ATTR\_DOUBLE\_QUOTE | Inside double quotes. |
| ATTR\_SINGLE\_QUOTE | Inside single quotes. |
| ATTR\_TAG | Inside a tag. |

_pszConfigScope_

\[Out\] This member contains the name of the configuration (scope) at the specified position on the active document if nFlags contains AI\_NEED\_CONFIG\_SCOPE.

_pszConfigDoc_

\[Out\] This member contains the name of the configuration selected for the active document if nFlags contains AI\_NEED\_CONFIG\_DOC.

## Version

Supported on Version 9.00 or later.
