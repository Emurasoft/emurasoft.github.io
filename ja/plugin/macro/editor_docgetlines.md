# Editor\_DocGetLines

指定する文書の全体の行数を取得します。このインライン関数を使うか、または [EE\_GET\_LINES](../message/ee_get_lines) メッセージを直接送ることができます。

Editor\_DocGetLines( HWND hwnd, int iDoc, int nLogical );

Editor\_GetLines( HWND hwnd, HEEDOC hDoc, int nLogical );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iDoc_

操作対象のドキュメントの 0 を基底とするインデックスを指定します。-1 を指定すると、現在アクティブなドキュメントが操作対象になります。

_hDoc_

対象となる文書へのハンドルを指定します。NULL を指定すると、現在アクティブな文書を対象とします。

_nLogical_

次のうちのいずれかを指定します。

| 定数 | 説明 |
| --- | --- |
| POS\_VIEW | 表示座標 |
| POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
| POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |

## 戻り値

文書全体の行数を返します。最終行が改行コードで終わる場合、最終行も含まれます。空の場合は 1 を返します。
