# Editor\_RemoveClip

クリップボード履歴にある特定の位置のテキストを消去します。このインライン関数を使うか、または [EE\_CLIP\_HISTORY](../message/ee_clip_history) メッセージを直接送ることができます。

Editor\_RemoveClip( HWND hwnd, UINT iPos, UINT nFlags );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iPos_

> クリップボード履歴にある位置を指定します。

_nFlags_

> 削除するクリップボードのフォーマットを指定します。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 文字単位で通常に選択されています。 |
> | SEL\_TYPE\_LINE | 行単位で選択されています。 |
> | SEL\_TYPE\_BOX | 箱型選択されています。 |

## 戻り値

> 戻り値はテキストが消去されたクリップボード履歴にある位置です。失敗すると、戻り値は -1 です。

## バージョン

> Version 9.00 以上で利用できます。
