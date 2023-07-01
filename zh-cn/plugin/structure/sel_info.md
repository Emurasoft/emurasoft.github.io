# SEL\_INFO

用于
[Editor\_GetMultiSel](../macro/editor_getmultisel)
内联函数 ( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) 消息)。

typedef struct \_SEL\_INFO {

size\_t cbSize;

POINT\_PTR ptStart;

POINT\_PTR ptEnd;

POINT\_PTR ptCaret;

} SET\_INFO;

## 字段

_cbSize_

> 必须指定 sizeof( SEL\_INFO )。

_ptStart_

> 指定所选内容的开始位置。

_ptEnd_

> 指定所选内容的结束位置。

_ptCaret_

> 指定所选内容的光标位置。

## 支持版本

> 支持 EmEditor 13 或之后的版本。
