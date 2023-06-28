# Editor\_GetSelEnd

選択テキストの終了位置を取得します。このインライン関数を使うか、または [EE\_GET\_SEL\_END](../message/ee_get_sel_end) メッセージを直接送ることができます。

Editor\_GetSelEnd( HWND hwnd, int nLogical, POINT\_PTR\* pptPos );

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

_pptPos_

> 選択テキストの終了位置を表す POINT\_\_PTR 構造体へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。