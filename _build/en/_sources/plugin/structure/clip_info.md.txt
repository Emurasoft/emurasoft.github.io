# CLIP\_INFO

Used by [EE\_CLIP\_HISTORY](../message/ee_clip_history) message.

typedef struct \_CLIP\_INFO {

size\_t cbSize;

LPWSTR pszBuf;

UINT cchBuf;

UINT iPos;

UINT nAction;

UINT nFlags;

} CLIP\_INFO;

## Members

_cbSize_

> Size of this data structure, in bytes. Set this member to sizeof( CLIP\_INFO ) before sending the [EE\_CLIP\_HISTORY](../message/ee_clip_history) message.

_pszBuf_

> Specifies the buffer that receives the text, or the text to be inserted.

_cchBuf_

> Specifies the size of the buffer in characters including the terminating NULL character.

_iPos_

> Specifies a position in the Clipboard history. If (UINT)-1 is specified while _nAction_ specifies CI\_GET\_CLIP, the actual clipboard contents are retrieved rather than getting from the
> Clipboard history.

_nAction_

> Specifies one of the following values. However, only CI\_INSERT\_CLIP can be combined with CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP.
>
> |     |     |
> | --- | --- |
> | CI\_GET\_CLIP | Retrieves text at the specified position in the Clipboard history. |
> | CI\_INSERT\_CLIP | Inserts text at the specified position in the Clipboard history. |
> | CI\_REMOVE\_CLIP | Removes text at the specified position in the Clipboard history. |
> | CI\_GET\_POS | Retrieves the current position in the Clipboard history. |
> | CI\_SET\_POS | Sets the current position in the Clipboard history. |
> | CI\_ROTATE\_CLIP | Rotates the current position in the Clipboard history. |
> | CI\_MOVE\_CLIP | Moves the specified position in the Clipboard history to another position. |
> | CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP | Prevents the current real Clipboard contents replaced by the Clipboard History. This value can be used in combination with CI\_INSERT\_CLIP. |

_nFlags_

> When nAction is CI\_INSERT\_CLIP or CI\_REMOVE\_CLIP, this value specifies the format of the Clipboard to be inserted or removed. When nAction is CI\_GET\_CLIP, this value is filled with the actual Clipboard format. When nAction is CI\_MOVE\_CLIP, this value is the destination position. Otherwise this value is ignored, and it must be zero. If this value is needed, it is one of the following values.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | The Clipboard format is normal text. |
> | SEL\_TYPE\_LINE | The Clipboard format is lines of text. |
> | SEL\_TYPE\_BOX | The Clipboard format is vertical selection of text. |

## Version

> Supported on Version 9.00 or later.