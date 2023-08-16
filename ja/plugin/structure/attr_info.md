# ATTR\_INFO

[EE\_GET\_ATTR](../message/ee_get_attr) メッセージで使用します。

```
typedef struct _ATTR_INFO {
	size_t cbSize; // in
	POINT_PTR ptLogical; // in
	UINT nFlags; // in
	UINT nAttr; // out
	WCHAR szConfigScope[MAX_CONFIG_NAME]; // out
	WCHAR szConfigDoc[MAX_CONFIG_NAME]; // out
} ATTR_INFO;
```

## フィールド

_cbSize_

\[入力\] このデータ構造体のバイトのサイズ。 [EE\_GET\_ATTR](../message/ee_get_attr) メッセージを送る前にこのメンバーを sizeof( ATTR\_INFO ) に設定します。

_ptLogical_

\[入力\] 情報を取得する論理座標の位置を指定します。

_nFlags_

\[入力\] 値の組み合わせをを下記の中から指定します。

|     |     |
| --- | --- |
| AI\_NEED\_CONFIG\_SCOPE | アクティブな文書にある特定の位置で、構成 (範囲) の名前が必要です。 |
| AI\_NEED\_CONFIG\_DOC | アクティブな文書のために選択した構成の名前が必要です。 |
| AI\_NEED\_ATTR\_SUB | nID によって指定された一時テキストを保存します。 |
| AI\_NEED\_ALL | 上記に記載されてある全ての情報が必要です。 |

_pszConfigScope_

nFlags が AI\_NEED\_CONFIG\_SCOPE を含む場合に、このメンバーは アクティブな文書にある特定の位置で、構成 (範囲) の名前を含みます。

_pszConfigDoc_

\[出力\] nFlags が AI\_NEED\_CONFIG\_DOC を含む場合に、このメンバーはアクティブな文書のために選択した構成の名前を含みます。

## バージョン

Version 9.00 以上で利用できます。
