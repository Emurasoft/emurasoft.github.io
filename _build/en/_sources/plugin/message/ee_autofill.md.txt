# EE\_AUTOFILL

Performs the AutoFill or Flash Fill action on the CSV document. You can send this message explicitly or by using the [Editor\_AutoFill](../macro/editor_autofill) inline function.

EE\_AUTOFILL

wParam = 0;

lParam = (LPARAM) (AUTOFILL\_INFO\*) pInfo;

## Parameters

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

Supported on EmEditor Version 17.5 or later.