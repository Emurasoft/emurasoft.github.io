# Editor\_AutoFill

Performs the AutoFill or Flash Fill action on the CSV document. You can use this inline function or explicitly send the [EE\_AUTOFILL](../message/ee_autofill)
message.

Editor\_AutoFill( HWND hwnd, AUTOFILL\_INFO\* pInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pInfo_

> Pointer to the [AUTOFILL\_INFO](../structure/autofill_info) structure.

## Return Values

> The return value can be a combination of the following values if the message succeeds. The return value of 0 means the message couldn't detect the pattern to complete the AutoFill or Flash Fill action. A negative value means the message failed.
>
> |     |     |
> | --- | --- |
> | S\_FILL\_COPY | Copies the values from the source range to the target range, repeating if necessary. |
> | S\_FILL\_SERIES | Extends the values in the source range into the target range as a series. |
> | S\_FILL\_FLASH | Performs the Flash Fill action, i.e. extends the values from the source range into the target range based on the detected pattern. This flag is valid only for the vertical direction. |

## Version

> Supported on EmEditor Version 17.5 or later.