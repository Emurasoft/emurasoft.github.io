# UNPIVOT\_INFO

Used by
[EE\_UNPIVOT](../message/ee_unpivot) message.

typedef struct \_UNPIVOT\_INFO {

UINT cbSize;

UINT nFlags;

LPCWSTR pszSelect;

LPCWSTR pszAttrLabel;

LPCWSTR pszValueLabel;

int nFooter;

} UNPIVOT\_INFO;

## Fields

_cbSize_

> Specifies sizeof( UNPIVOT\_INFO ).

_nFlags_

> Not used. Must be 0.

_pszSelect_

> Specifies the string to select which columns to be unpivot. Examples are "2-5", "3-", "1,3,5". This field cannot be empty.

_pszAttrLabel_

> Specifies the heading label for the attribute column to be created.

_pszValueLabel_

> Specifies the heading label for the value column to be created.

_nFooter_

> Specifies the number of rows in the footer. The footer rows area not converted.

## Version

> Supported on Version 21.4 or later.
