# Editor\_Unpivot

Converts columns into rows by flattening the CSV data. You can use this inline function or explicitly send the [EE\_UNPIVOT](../message/ee_unpivot) message.

HRESULT Editor\_Unpivot( HWND hwnd, LPCWSTR pszSelect, LPCWSTR pszAttrLabel, LPCWSTR pszValueLabel, int nFooter );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pszSelect_

> Specifies the string to select which columns to be unpivot. Examples are "2-5", "3-", "1,3,5". This field cannot be empty.

_pszAttrLabel_

> Specifies the heading label for the attribute column to be created.

_pszValueLabel_

> Specifies the heading label for the value column to be created.

_nFooter_

> Specifies the number of rows in the footer. The footer rows are not converted.

## Return Values

> The return value is a negative value if it fails.

## Version

> Supported on Version 21.4 or later.
