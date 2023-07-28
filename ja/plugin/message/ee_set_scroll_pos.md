# EE\_SET\_SCROLL\_POS

スクロールバーの位置を設定します。このメッセージを直接送るか、または [Editor\_SetScrollPos インライン関数](../macro/editor_setscrollpos)、または [Editor\_SetScrollPosEx インライン関数](../macro/editor_setscrollposex) を使うことができます。

EE\_SET\_SCROLL\_POS

wParam = (WPARAM) (BOOL) bCanMoveCursor;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## パラメータ

_bCanMoveCursor_

TRUE の場合、プロパティで [**\[スクロールでカーソルも移動\]** チェック ボックス](../../dlg/properties/scroll/index) がチェックされている場合 、カーソル位置も移動します。FALSE の場合、カーソル位置は移動しません。

_pptPos_

スクロールバーの位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

## バージョン

Version 3.00 以上で利用できます。ただし、bCanMoveCursor は、Version 5.00 以上で利用できます。Version 5.00 未満では、bCanMoveCursor は常に FALSE を指定することになります。
