# SEL\_INFO

用於
[Editor\_GetMultiSel](../macro/editor_getmultisel)
內嵌函式 ( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) 消息)。

typedef struct \_SEL\_INFO {

size\_t cbSize;

POINT\_PTR ptStart;

POINT\_PTR ptEnd;

POINT\_PTR ptCaret;

} SET\_INFO;

## 欄位

_cbSize_

> 必須指定 sizeof( SEL\_INFO )。

_ptStart_

> 指定所選內容的開始位置。

_ptEnd_

> 指定所選內容的結束位置。

_ptCaret_

> 指定所選內容的游標位置。

## 支持版本

> 支持 EmEditor 13 或之後的版本。
