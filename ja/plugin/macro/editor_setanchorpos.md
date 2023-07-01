# Editor\_SetAnchorPos

選択範囲の開始位置を設定します。このインライン関数を使うか、または [EE\_SET\_ANCHOR\_POS メッセージ](../message/ee_set_anchor_pos) を直接送ることができます。

Editor\_SetAnchorPos( HWND hwnd, int nLogical, POINT\_PTR\* pptPos );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nLogical_

> 次のうちのいずれかを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | POS\_VIEW | 表示座標 |
> | POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
> | POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |
> | POS\_CELL | CSV セル単位 |

_pptPos_

> 選択範囲の開始位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 4.03 以上で利用できます。
