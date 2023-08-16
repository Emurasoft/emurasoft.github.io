# TEMP\_INFO

Used by [EE\_EDIT\_TEMP](../message/ee_edit_temp) message and [EVENT\_TEMP\_SAVING event](../event/index).

```
typedef struct _TEMP_INFO {
	size_t cbSize;
	LPCWSTR pszTempText;
	LPCWSTR pszTitle;
	LPCWSTR pszIconPath;
	LPCWSTR pszConfig;
	POINT_PTR ptInitialCaret;
	UINT nID;
	UINT nEncoding;
	UINT nFlags;
} TEMP_INFO;
```

## Members

_cbSize_

Size of this data structure, in bytes. Set this member to sizeof( TEMP\_INFO ) before sending the [EE\_EDIT\_TEMP](../message/ee_edit_temp) message.

_pszTempText_

Specifies temporary text on memory that you want to open as a new document.

_pszTitle_

Specifies the title of the new document.

_pszIconPath_

Specifies the path and file name of the icon that you want to use as a new document.

_pszConfig_

Specifies the name of the configuration that the new document should use.

_ptInitialCaret_

Specifies the initial cursor position.

_nID_

Specifies an ID when you want to activate or close the temporary text.

_nEncoding_

Specifies the encoding of the file.

_nFlags_

Specifies one of the following values.

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | Opens the temporary text if nID is zero. Activates the existing temporary text if nID is not zero. |
| TEMP\_INFO\_CLOSE | Closes the temporary text specified by nID. |
| TEMP\_INFO\_SAVE | Saves the temporary text specified by nID. |

## Version

Supported on Version 9.00 or later.
