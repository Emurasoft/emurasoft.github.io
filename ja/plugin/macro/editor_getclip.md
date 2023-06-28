# Editor\_GetClip

クリップボード履歴にある特定の位置でテキストを取得します。このインライン関数を使うか、または [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを直接送ることができます。

Editor\_GetClip( HWND hwnd, LPWSTR pszBuf, UINT cchBuf, UINT iPos, UINT\* pnFlags );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pszBuf_

> テキストを受信するバッファを指定します。

_cchBuf_

> 終端 NULL 文字を含めた文字のバッファのサイズを指定します。

_iPos_

> クリップボード履歴の中 の位置を指定します。(UINT)-1 を指定すると、クリップボード履歴ではなく実際のクリップボードの中身を取得します。

_nFlags_

> この値は実際のクリップボード フォーマットで満たされます。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 文字単位で通常に選択されています。 |
> | SEL\_TYPE\_LINE | 行単位で選択されています。 |
> | SEL\_TYPE\_BOX | 箱型選択されています。 |

## 戻り値

> 戻り値は、終端文字を含めたテキストを受信する必要がある文字の pszBuf バッファのサイズです。メッセージが失敗すると、戻り値は -1 です。

## バージョン

> Version 9.00 以上で利用できます。