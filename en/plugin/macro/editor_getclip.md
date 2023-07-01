# Editor\_GetClip

Retrieves text at the specified position in the Clipboard history. You can use this inline function or explicitly send the [EE\_CLIP\_HISTORY](../message/ee_clip_history)
message.

Editor\_GetClip( HWND hwnd, LPWSTR pszBuf, UINT cchBuf, UINT iPos, UINT\* pnFlags );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pszBuf_

> Specifies the buffer that receives the text

_cchBuf_

> Specifies the size of the buffer in characters including the terminating NULL character.

_iPos_

> Specifies the position in the Clipboard history. If (UINT)-1 is specified, the actual clipboard contents are retrieved rather than getting from the Clipboard history.

_nFlags_

> This value is filled with the actual Clipboard format.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | The Clipboard format is normal text. |
> | SEL\_TYPE\_LINE | The Clipboard format is lines of text. |
> | SEL\_TYPE\_BOX | The Clipboard format is vertical selection of text. |

## Return Values

> The return value is the size of the pszBuf buffer in characters needed to receive the text including the terminating NULL. If the message fails, the return value is -1.

## Version

> Supported on EmEditor Version 9.00 or later.
