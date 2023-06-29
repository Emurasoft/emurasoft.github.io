# Editor\_RemoveClip

Removes text at the specified position in the Clipboard history. You can use this inline function or explicitly send the [EE\_CLIP\_HISTORY](../message/ee_clip_history)
message.

Editor\_RemoveClip( HWND hwnd, UINT iPos, UINT nFlags );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iPos_

> Specifies the position in the Clipboard history.

_nFlags_

> Specifies the format of the Clipboard to removed.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | The Clipboard format is normal text. |
> | SEL\_TYPE\_LINE | The Clipboard format is lines of text. |
> | SEL\_TYPE\_BOX | The Clipboard format is vertical selection of text. |

## Return Values

> The return value is the position in the Clipboard history where the text is removed. If the message fails, the return value is -1.

## Version

> Supported on EmEditor Version 9.00 or later.