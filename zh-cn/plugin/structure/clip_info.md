# CLIP\_INFO

用于 [EE\_CLIP\_HISTORY](../message/ee_clip_history) 消息。

typedef struct \_CLIP\_INFO {

size\_t cbSize;

LPWSTR pszBuf;

UINT cchBuf;

UINT iPos;

UINT nAction;

UINT nFlags;

} CLIP\_INFO;

## 成员

_cbSize_

> 以字节为单位的数据结构大小。在发送 [EE\_CLIP\_HISTORY](../message/ee_clip_history) 消息之前，把这个成员设为sizeof( CLIP\_INFO )。

_pszBuf_

> 指定接收文本的缓冲区，或要插入的文本。

_cchBuf_

> 指定以字符为单位的缓冲区大小，包括终止空字符。

_iPos_

> 指定剪贴板历史记录中的一个位置。如果指定了 (UINT)-1 当 _nAction_ 指定 CI\_GET\_CLIP 时，会检索实际的剪贴板内容而不是从剪贴板记录中获取。

_nAction_

> 指定下列值之一。 然而，只有 CI\_INSERT\_CLIP 能与 CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP 组合。
>
> |     |     |
> | --- | --- |
> | CI\_GET\_CLIP | 在剪贴板历史记录中的指定位置处检索文本。 |
> | CI\_INSERT\_CLIP | 在剪贴板历史记录中的指定位置处插入文本。 |
> | CI\_REMOVE\_CLIP | 在剪贴板历史记录中的指定位置处删除文本。 |
> | CI\_GET\_POS | 在剪贴板历史记录中检索当前位置。 |
> | CI\_SET\_POS | 在剪贴板历史记录中设置当前位置。 |
> | CI\_ROTATE\_CLIP | 在剪贴板历史记录中轮换当前位置。 |
> | CI\_MOVE\_CLIP | 把剪贴板历史记录中的指定位置移动到另一个位置。 |
> | CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP | 防止当前真正的剪贴板上的内容被剪贴板历史记录所替换。这个值能与 CI\_INSERT\_CLIP 合用。 |

_nFlags_

> 当 nAction 是 CI\_INSERT\_CLIP 或 CI\_REMOVE\_CLIP 时，这个值指定要被插入或删除的剪贴板格式。当 nAction 是 CI\_GET\_CLIP 时，这个值被实际的剪贴板格式所填充。当 nAction 是 CI\_MOVE\_CLIP 时，这个值则是目标位置。不然的话，这个值会被忽略，并且它一定是零。如果需要该值，它会是下列值之一。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 剪贴板格式是标准文本。 |
> | SEL\_TYPE\_LINE | 剪贴板格式是文本行。 |
> | SEL\_TYPE\_BOX | 剪贴板格式是文本的垂直选区。 |

## 版本

> 支持 EmEditor 9.00 或之后的版本。