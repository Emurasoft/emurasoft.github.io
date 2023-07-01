# Editor\_SetCaretPosEx

カーソル位置を移動し、選択範囲を伸縮することもできます。このインライン関数を使うか、または [EE\_SET\_CARET\_POS メッセージ](../message/ee_set_caret_pos) を直接送ることができます。

Editor\_SetCaretPosEx( HWND hwnd, int nLogical, POINT\_PTR\* pptPos, bExtend );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nLogical_

> 次の値の組み合わせを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | POS\_VIEW | 表示座標 |
> | POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
> | POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |
> | POS\_CELL | CSV セル単位 |
> | POS\_SCROLL\_ALWAYS | POS\_SCROLL\_CENTER または POS\_SCROLL\_TOP と共に指定し、カーソル位置が既にウィンドウ内に存在していても常に移動します。 |
> | POS\_SCROLL\_CENTER | カーソル位置がウィンドウの中央になるようにします。 |
> | POS\_SCROLL\_DONT\_CARE | カーソル位置はウィンドウ内のスクロールの量がもっとも少なくなる位置になります。 |
> | POS\_SCROLL\_TOP | カーソル位置がウィンドウの最上部になるようにします。 |

_pptPos_

> カーソル位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_bExtend_

> 省略可能。選択範囲を伸縮するかどうかを指定します。bExtend が TRUE
> の場合、カーソルが指定する位置に移動しますが、選択範囲の最初の位置は変わりません。FALSE の場合、両方とも指定する位置に移動します。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 4.03 以上で利用できます。ただし、POS\_SCROLL\_DONT\_CARE、POS\_SCROLL\_CENTER、POS\_SCROLL\_TOP フラグは Version 6.00 で追加されました。POS\_SCROLL\_ALWAYS は Version 7.00.4 で追加されました。
