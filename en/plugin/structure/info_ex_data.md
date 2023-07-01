# INFO\_EX\_DATA

Used by [**EE\_INFO\_EX** message](../message/ee_info_ex).

typedef struct \_INFO\_EX\_DATA {

UINT cbSize;

UINT nCmd;

HEEDOC hDoc;

LPARAM lParam;

} INFO\_EX\_DATA;

## Fields

_cbSize_

> Must be sizeof(INFO\_EX\_DATA).

_nCmd_

> Specifies a parameter to retrieve or set. Please see the
> [**EE\_INFO** message](../message/ee_info) for the list of commands.

_hDoc_

> Specifies the handle to the target document. If NULL is specified, the currently active document will be targeted. This field may not be used depending on _nCmd_.

_lParam_

> Depends on the parameter specified.

## Version

> Supported on EmEditor Professional Version 21.8 or later.
