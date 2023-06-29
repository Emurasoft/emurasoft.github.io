# EP\_SYNC\_NOW

Instructs the plug-in to sync now if the sync feature is supported.

EP\_SYNC\_NOW

hwnd = hwndView;

wParam = nFlags;

lParam = 0;

## Parameters

_hwndView_

> The window handle to the EmEditor view. This value can be NULL if the active view cannot be determined.

_nFlags_

> This flag can include a combination of the following values. SYNC\_SETTINGS\_SEND and SYNC\_SETTINGS\_RECEIVE cannot be specified at the same time.
>
> | Value | Meaning |
> | --- | --- |
> | SYNC\_SETTINGS\_SEND | The plug-in should send the settings. |
> | SYNC\_SETTINGS\_RECEIVE | The plug-in should receive the settings. |
> | SYNC\_FLAG\_FORCE | The plug-in should receive the settings even if the settings file timestamp is old. |
> | SYNC\_FLAG\_REFRESH\_UI | The plug-in should update UI after receiving the settings. |

## Return Values

> The return value is ignored.

## Version

> Supported on Version 20.9 or later.