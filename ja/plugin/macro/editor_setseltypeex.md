# Editor\_SetSelTypeEx

選択状態の種類を設定します。このインライン関数を使うか、または [EE\_SET\_SEL\_TYPE メッセージ](../message/ee_set_sel_type) を使うことができます。

Editor\_SetSelTypeEx( hwnd, bNeedAlways, nSelType );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bNeedAlways_

TRUE の場合は、選択されていなくても、選択状態の種類を設定できます。FALSE の場合は、SEL\_TYPE\_NONE を指定すると選択を解除します。

_nSelType_

次の値の組み合わせになります。SEL\_TYPE\_NONE、SEL\_TYPE\_CHAR、SEL\_TYPE\_LINE および SEL\_TYPE\_BOX
は同時に指定することはできません。SEL\_TYPE\_KEYBOARD のみ、他の値と組み合わせて指定できます。

| 値 | 説明 |
| --- | --- |
| SEL\_TYPE\_NONE | 選択されていません (bNeedAlways = TRUE の場合) |
| SEL\_TYPE\_CHAR | 文字単位で通常に選択されています |
| SEL\_TYPE\_LINE | 行単位で選択されています |
| SEL\_TYPE\_BOX | 箱型選択されています |
| SEL\_TYPE\_KEYBOARD | キーボードで選択されています |

## 戻り値

戻り値は利用されません。

## バージョン

Version 3.00 以上で利用できます。ただし、bNeedAlways は、Version 5.00 以上で利用できます。Version 5.00 未満では、bNeedAlways は常に FALSE を指定することになります。
