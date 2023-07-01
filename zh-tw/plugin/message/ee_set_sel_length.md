# EE\_SET\_SEL\_LENGTH

變更選區的字符長度。您能明確地發送該消息或用
[Editor\_SetSelLength](../macro/editor_setsellength)
內嵌函式。

EE\_SET\_SEL\_LENGTH

wParam = (WPARAM) (UINT) nLen;

lParam = 0;

## 參數

_nLen_

> 指定選區的字符長度。換行總是計為兩個字符長度 (CR+LF)。

## 返回值

> 不使用返回值。
