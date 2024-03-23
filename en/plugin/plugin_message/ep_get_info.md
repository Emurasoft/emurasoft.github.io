# EP\_GET\_INFO

Retrieves information about the plug-in.

EP\_GET\_INFO

hwnd = hwndParent;

wParam = flag;

lParam = 0;

## Parameters

_hwndParent_

The window handle of the EmEditor frame window.

_flag_

Specifies the type of information requested. It is one of the following values.

| Value | Meaning |
| --- | --- |
| EPGI\_ALLOW\_OPEN\_SAME\_GROUP | Returns TRUE if the plug-in allows EmEditor to open a new file in the same group. |
| EPGI\_ALLOW\_MULTIPLE\_INSTANCES | Returns TRUE if the plug-in supports multiple instances. If the plug-in should be allowed to run in more than one frame simultaneously, this message should return TRUE. Note that global variables will be shared when multiple instances are running. |
| EPGI\_MAX\_EE\_VERSION | Returns the newest version number of supported EmEditor \* 1000. |
| EPGI\_MIN\_EE\_VERSION | Returns the oldest version number of supported EmEditor \* 1000. |
| EPGI\_SUPPORT\_EE\_PRO | Returns TRUE if EmEditor Professional is supported. |
| EPGI\_SUPPORT\_EE\_STD | Returns TRUE if EmEditor Standard is supported. |

## Return Values

The return value depends on the flag parameter.

## Version

Supported on EmEditor Professional Version 5.00 or later.
