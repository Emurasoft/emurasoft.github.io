# Editor\_GetLines

現在の文書の行数を取得します。このインライン関数を使うか、または [EE\_GET\_LINES](../message/ee_get_lines) メッセージを直接送ることができます。

Editor\_GetLines( HWND hwnd, int nLogical );

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

## 戻り値

> 文書全体の行数を返します。最終行が改行コードで終わる場合、最終行も含まれます。空の場合は 1 を返します。
