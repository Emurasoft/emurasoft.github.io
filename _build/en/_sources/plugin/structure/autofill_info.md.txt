# AUTOFILL\_INFO

Used by [EE\_AUTOFILL](../message/ee_autofill) message.

typedef struct \_AUTOFILL\_INFO {

UINT cbSize;

POINT\_PTR ptSrcCellStart;

POINT\_PTR ptSrcCellEnd;

POINT\_PTR ptDestCellStart;

POINT\_PTR ptDestCellEnd;

DWORD dwFlags;

INT64 nIncrement;

} AUTOFILL\_INFO;

## Members

_cbSize_

> Size of this data structure, in bytes. Set this member to sizeof( AUTOFILL\_INFO ) before sending the [EE\_AUTOFILL](../message/ee_autofill) message.

_ptSrcCellStart_

> Specifies the starting position of the source cells.

_ptSrcCellEnd_

> Specifies the ending position of the source cells.

_ptDestCellStart_

> Specifies the starting position of the destination cells.

_ptDestCellEnd_

> Specifies the ending position of the destination cells.

_dwFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FILL\_DEFAULT | EmEditor determines the values to fill the destination cells. |
> | FLAG\_FILL\_COPY | Copies the values from the source range to the target range, repeating if necessary. |
> | FLAG\_FILL\_SERIES | Extends the values in the source range into the target range as a series. |
> | FLAG\_FILL\_FLASH | Performs the Flash Fill action, i.e. extends the values from the source range into the target range based on the detected pattern. This flag is valid only for the vertical direction. |
> | FLAG\_FILL\_DONT\_OVERWRITE | The AutoFill action will not overwrite the existing cells in the target range. Cannot combine with FLAG\_FILL\_FLASH. |
> | FLAG\_FILL\_REPEAT | The AutoFill action will be repeated with the new value on a non-empty cell. Cannot combine with FLAG\_FILL\_FLASH. |

_nIncrement_

> Specifies the number of increment for a series if only one cell is specified for the source range and if **FLAG\_FILL\_SERIES** is specified for the _dwFlags_ member.

## Version

> Supported on Version 17.5 or later.