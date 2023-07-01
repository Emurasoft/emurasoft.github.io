# Editor\_GetFilter

Retrieves the filter strings and settings for the current document. You can use this inline function or explicitly send
the [EE\_GET\_FILTER](../message/ee_filter) message.

Editor\_GetFilter( HWND hwnd, int iFilter, LPWSTR pszFilter, UINT cchFilter, int\* piColumn, UINT64\* pnFlags, INT\_PTR\* pxBegin, INT\_PTR\* pxEnd )

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pszFilter_

> Specifies a buffer to retrieve the filter string.

_cchFilter_

> Specifies the size of the buffer in characters to retrieve the filter string.

_piColumn_

> Specifies the pointer to the integer to retrieve the index of the column of the text where the filter is applied. This index becomes -1 if the whole lines are searched for the filter.

_pnFlags_

> Specifies the pointer to the 64-bit integer to retrieve the flags. The retrieved flags can be a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_ESCAPE | Uses escape sequences. |
> | FLAG\_FIND\_LOGICAL\_OR | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
> | FLAG\_FIND\_NEGATIVE | Shows the Filter toolbar and excludes the lines that match the specified string. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_REG\_EXP | Uses a regular expression. |

_pxBegin_

> Specifies the pointer to the integer to retrieve the index of beginning of the column (in logical characters) of the text to be searched. This value can be -1 if the last portion of the text should be counted as specified as _xEnd_.

_pxEnd_

> Specifies the pointer to the integer to retrieve the index of ending of the column (in logical characters) of the text to be searched. This value can be -1 if all the rest of the text should be searched.

## Return Values

> The return value
> is TRUE if the iFilter is 0 or larger and the message was successful. The return value is the number of filters if the iFilter is -1.

## Version

> Supported on EmEditor Professional Version 16.0 or later.
