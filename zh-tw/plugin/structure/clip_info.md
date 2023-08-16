# CLIP\_INFO

用於 [EE\_CLIP\_HISTORY](../message/ee_clip_history) 消息。

```
typedef struct _CLIP_INFO {
	size_t cbSize;
	LPWSTR pszBuf;
	UINT cchBuf;
	UINT iPos;
	UINT nAction;
	UINT nFlags;
} CLIP_INFO;
```

## 構成

_cbSize_

以位元為單位的數據結構大小。在發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history) 消息之前，把這個成員設為sizeof( CLIP\_INFO )。

_pszBuf_

指定接收文字的緩沖區，或要插入的文字。

_cchBuf_

指定以字元為單位的緩沖區大小，包括終止空字元。

_iPos_

指定剪貼簿歷史記錄中的一個位置。如果指定了 (UINT)-1 當 _nAction_ 指定 CI\_GET\_CLIP 時，會檢索實際的剪貼簿內容而不是從剪貼簿記錄中獲取。

_nAction_

指定下列值之一。 然而，只有 CI\_INSERT\_CLIP 能與 CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP 組合。

|     |     |
| --- | --- |
| CI\_GET\_CLIP | 在剪貼簿歷史記錄中的指定位置處檢索文字。 |
| CI\_INSERT\_CLIP | 在剪貼簿歷史記錄中的指定位置處插入文字。 |
| CI\_REMOVE\_CLIP | 在剪貼簿歷史記錄中的指定位置處刪除文字。 |
| CI\_GET\_POS | 在剪貼簿歷史記錄中檢索目前的位置。 |
| CI\_SET\_POS | 在剪貼簿歷史記錄中設定目前的位置。 |
| CI\_ROTATE\_CLIP | 在剪貼簿歷史記錄中輪換目前的位置。 |
| CI\_MOVE\_CLIP | 把剪貼簿歷史記錄中的指定位置移動到另一個位置。 |
| CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP | 防止目前的真正的剪貼簿上的內容被剪貼簿歷史記錄所取代。這個值能與 CI\_INSERT\_CLIP 合用。 |

_nFlags_

當 nAction 是 CI\_INSERT\_CLIP 或 CI\_REMOVE\_CLIP 時，這個值指定要被插入或刪除的剪貼簿格式。當 nAction 是 CI\_GET\_CLIP 時，這個值被實際的剪貼簿格式所填充。當 nAction 是 CI\_MOVE\_CLIP 時，這個值則是目標位置。不然的話，這個值會被忽略，並且它一定是零。如果需要該值，它會是下列值之一。

|     |     |
| --- | --- |
| SEL\_TYPE\_CHAR | 剪貼簿格式是標準文字。 |
| SEL\_TYPE\_LINE | 剪貼簿格式是文字行。 |
| SEL\_TYPE\_BOX | 剪貼簿格式是文字的垂直選區。 |

## 支持版本

支持 EmEditor 9.00 或之後的版本。
