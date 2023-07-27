# Editor\_GetSelTypeEx

選択状態の種類を取得します。このインライン関数を使うか、または [EE\_GET\_SEL\_TYPE メッセージ](../message/ee_get_sel_type) を直接送ることができます。

Editor\_GetSelTypeEx( HWND hwnd, BOOL bNeedAlways );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bNeedAlways_

TRUE の場合は、選択されていなくても、選択状態の種類を返します。FALSE の場合は、選択されていない場合は、選択状態を返さず SEL\_TYPE\_NONE を返します。

## 戻り値

次の値の組み合わせになります。SEL\_TYPE\_NONE、SEL\_TYPE\_CHAR、SEL\_TYPE\_LINE および SEL\_TYPE\_BOX
は同時に指定することはできません。SEL\_TYPE\_KEYBOARD と SEL\_TYPE\_SELECTED は、他の値と組み合わせて指定できます。bNeedAlways が TRUE の場合は、選択状態だと SEL\_TYPE\_SELECTED の論理和が返されます。bNeedAlways が FALSE の場合、SEL\_TYPE\_SELECTED は使用されません。

| 値 | 説明 |
| --- | --- |
| SEL\_TYPE\_NONE | 選択されていません (bNeedAlways = FALSE の場合) |
| SEL\_TYPE\_CHAR | 文字単位で通常に選択されています |
| SEL\_TYPE\_LINE | 行単位で選択されています |
| SEL\_TYPE\_BOX | 箱型選択されています |
| SEL\_TYPE\_KEYBOARD | キーボードで選択されています |
| SEL\_TYPE\_SELECTED | 選択されています (bNeedAlways = TRUE の場合) |

## バージョン

Version 3.00 以上で利用できます。ただし、bNeedAlways は、Version 5.00 以上で利用できます。Version 5.00 未満では、bNeedAlways は常に FALSE を指定することになります。
