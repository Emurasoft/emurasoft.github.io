# EE\_REG\_SET\_VALUE

Sets a value into the Registry or an INI file depending on the EmEditor settings. You can send this message explicitly or
by using the [Editor\_RegSetValue](../macro/editor_regsetvalue) inline function.

EE\_REG\_SET\_VALUE

wParam = 0;

(REG\_SET\_VALUE\_INFO\*)lParam = pRegSetValueInfo;

## Parameters

_pRegSetValueInfo_

> Pointer to the [REG\_SET\_VALUE\_INFO structure](../structure/reg_set_value_info).

## Return Values

> If the message succeeds, the return value is ERROR\_SUCCESS.
>
> If the message fails, the return value is a nonzero error code defined in Winerror.h.

## Version

Supported on EmEditor Version 7.00 or later.