# EE\_GET\_SCROLL\_POS

スクロールバーの位置を取得します。このメッセージを直接送るか、または [Editor\_GetScrollPos インライン関数](../macro/editor_getscrollpos) を使うことができます。

```
EE_GET_SCROLL_POS
wParam = 0;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## パラメータ

_pptPos_

スクロールバー位置を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。
