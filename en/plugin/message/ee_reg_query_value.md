# EE\_REG\_QUERY\_VALUE

Retrieves the data for the specified value from the Registry or an INI file depending on the EmEditor settings. You can send this message explicitly or
by using the [Editor\_RegQueryValue](../macro/editor_regqueryvalue) inline function.

```
EE_REG_QUERY_VALUE
wParam = 0;
(REG_QUERY_VALUE_INFO*)lParam = pRegQueryValueInfo;
```

## Parameters

_pRegSetValueInfo_

Pointer to the [REG\_QUERY\_VALUE\_INFO structure](../structure/reg_query_value_info).

## Return Values

If the message succeeds, the return value is ERROR\_SUCCESS.

If the message fails, the return value is a nonzero error code defined in Winerror.h.

## Version

Supported on EmEditor Version 7.00 or later.
