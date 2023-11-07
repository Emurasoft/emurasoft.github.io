# CONVERT\_CSV\_INFO

[EE\_CONVERT\_CSV](../message/ee_convert_csv) メッセージで使用します。

```
typedef struct _CONVERT_CSV_INFO {
	UINT cbSize;
	int iDestMode;
	UINT nFlags;
	int nSepCount;
	const int* pcxSepWidths;
} CONVERT_CSV_INFO;
```

## フィールド

_cbSize_

sizeof( CONVERT\_CSV\_INFO ) を指定します。

_iDestMode_

変換先の CSV フォーマットのインデックスを指定します。0 は CSV でなく固定幅列のフォーマットを意味します。1 は [カスタマイズ] ダイアログの [CSVフォーマット] ページで定義された最初のフォーマットを意味します (既定では、カンマ区切り)。

_nFlags_

次の値の組み合わせを指定することができます。

| 値 | 意味 |
| --- | --- |
| CSV\_HALF\_WIDTH | すべて半角文字とみなします |
| CSV\_DISCARD\_UNDO | 元に戻す情報を破棄します |
| CSV\_DISCARD\_UNDO | 列の幅よりも長い文字列は切り詰めます |
| CSV\_DISCARD\_UNDO | 文字列の長さが列の幅を超えると警告します |

_nSepCount_

現在の文書が CSV フォーマットでない場合で、固定幅列のフォーマットを CSV 文書に変換したい場合、このパラメータは区切りの数を指定します。この数は、_pcxSepWidths_ パラメータで指定された配列のサイズと等しい必要があります。現在の文書が CSV 文書の場合、このパラメータは無視されます。

_pcxSepWidths_

_nSepCount_ パラメータが 0 でない場合、列幅を表現する整数の配列を指定します。

## バージョン

EmEditor Professional Version 19.8 以上で利用できます。
