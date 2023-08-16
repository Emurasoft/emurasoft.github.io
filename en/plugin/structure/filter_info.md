# FILTER\_INFO

Used by [EE\_FILTER](../message/ee_filter) message. This structure is
obsolete. New plug-ins should use the [FILTER\_INFO\_EX](filter_info_ex) structure instead.

```
typedef struct _FILTER_INFO {
	UINT cbSize;
	UINT flags;
	int iColumn;
	LPCWSTR pszFilter;
	INT_PTR xBegin;
	INT_PTR xEnd;
} FILTER_INFO;
```

## Fields

_cbSize_

Specifies the size of this structure, sizeof( FILTER\_INFO ).

_flags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | Matches cases. |
| FLAG\_FIND\_CONTINUE | Specifies the EE\_FILTER message called next time should not clear the filter. This filter is not <br> applied immediately after this message is called. This flag is used when you want to create multiple levels of the filter. <br> It is similar to the FLAG\_FIND\_KEEP\_PREVIOUS flag, but since the actual filter is not <br> applied each time the message is called, this method works faster if there are multiple filter levels. |
| FLAG\_FIND\_ESCAPE | Uses escape sequences. |
| FLAG\_FIND\_KEEP\_PREVIOUS | Specifies the EE\_FILTER message should not clear the existing filter before applying the new filter. This flag is used when you want to create multiple levels of the filter. |
| FLAG\_FIND\_LOGICAL\_OR | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
| FLAG\_FIND\_NEGATIVE | Shows the Filter toolbar and excludes the lines that match the specified string. |
| FLAG\_FIND\_ONLY\_WORD | Searches only words. |
| FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
| FLAG\_FIND\_REMOVE\_LAST | Removes the last added filter level. |

_iColumn_

Specifies the index of the column of the text you want to search, or -1 if you want to search whole lines, or -2 if you want to specify the beginning and end of the text in characters as _xBegin_ and _xEnd_.

_pszFilter_

Specifies a string to search for.

_xBegin_

Specifies the index of beginning of the column (in logical characters) of the text you want to search, or -1 if you want to
count the last portion of the text and specify as _xEnd_. The _iColumn_ must be -2 to enable this field.

_xEnd_

Specifies the index of ending of the column (in logical characters) of the text you want to search, or -1 if you want to search
all the rest of the text. The _iColumn_ must be -2 to enable this field.

## Version

Supported on EmEditor Professional Version 14.7 or later.
