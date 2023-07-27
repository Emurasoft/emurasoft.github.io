# Editor\_GetColor

指定する部分の文字色、背景色、スタイルを取得します。このインライン関数を使うか、または [EE\_GET\_COLOR](../message/ee_get_color) メッセージを直接送ることができます。

Editor\_GetColor( HWND hwnd, BOOL bFind, UINT nIndex, COLORREF\* pclrText, COLORREF\* pclrBack, int\* pnAttr );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bFind_

検索の色を取得する場合には TRUE を、それ以外の部分の色を取得する場合には FALSE を指定します。

_nIndex_

色を取得するインデックスを指定します。bFind が FALSE の場合、インデックスは MAX\_SMART\_COLOR より小さい値である必要があります。

_pclrText_

文字色が格納されるポインタを指定します。この値は、RGB値、または次のいずれかの値になります。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | Windows システム色が使用されます。 |
| TRANSPARENT\_COLOR | 透明色です。 |

_pclrBack_

\[out\] 背景色が格納されるポインタを指定します。この値は、RGB値、または次のいずれかの値になります。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | Windows システム色が使用されます。 |
| TRANSPARENT\_COLOR | 透明色です。 |

_pnAttr_

\[out\] スタイルが格納されるポインタを指定します。この値は、次のいずれかの値になります。

|     |     |
| --- | --- |
| SMART\_COLOR\_FONT\_NORMAL | 通常のフォントです。 |
| SMART\_COLOR\_FONT\_UNDERLINE | 下線付きフォントです。 |
| SMART\_COLOR\_FONT\_BOLD | 太字フォントです。 |
| SMART\_COLOR\_FONT\_ITALIC | 斜体フォントです。 |
| SMART\_COLOR\_FONT\_WIGGLY | 波線が付いたフォントです。 |
| SMART\_COLOR\_FONT\_DOTTED | 線の場合、点線です。 |

## 戻り値

成功すると TRUE を、失敗すると FALSE を返します。

## バージョン

Version 14.4 以上で利用できます。
