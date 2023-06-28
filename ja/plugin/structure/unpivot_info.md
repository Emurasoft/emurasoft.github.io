# UNPIVOT\_INFO

[EE\_UNPIVOT メッセージ](../message/ee_unpivot) で使用します。

typedef struct \_UNPIVOT\_INFO {

UINT cbSize;

UINT nFlags;

LPCWSTR pszSelect;

LPCWSTR pszAttrLabel;

LPCWSTR pszValueLabel;

int nFooter;

} UNPIVOT\_INFO;

## フィールド

_cbSize_

> このデータ構造体のサイズ、sizeof( UNPIVOT\_INFO )を指定します。

_nFlags_

> 使用されません。0 である必要があります。

_pszSelect_

> ピボット解除する列を選択する文字列を指定します。例: "2-5"、"3-"、"1,3,5"。このフィールドは空にすることができません。

_pszAttrLabel_

> 属性として作成される列のヘディングのラベルを指定します。

_pszValueLabel_

> 値として作成される列のヘディングのラベルを指定します。

_nFooter_

> フッターの行数を指定します。フッターの領域は変換されません。

## バージョン

> Version 21.4 以上で利用できます。