# TEMP\_INFO

[EE\_EDIT\_TEMP](../message/ee_edit_temp) メッセージ と [EVENT\_TEMP\_SAVING イベント](../event/index) で使用します。

```
typedef struct _TEMP_INFO {
	size_t cbSize;
	LPCWSTR pszTempText;
	LPCWSTR pszTitle;
	LPCWSTR pszIconPath;
	LPCWSTR pszConfig;
	POINT_PTR ptInitialCaret;
	UINT nID;
	UINT nEncoding;
	UINT nFlags;
} TEMP_INFO;
```

## フィールド

_cbSize_

このデータ構造体のバイトのサイズ。 [EE\_EDIT\_TEMP](../message/ee_edit_temp) メッセージを送る前にこのメンバーを sizeof( TEMP\_INFO ) に設定します。

_pszTempText_

新規文書として開きたいメモリの一時テキストを指定します。

_pszTitle_

新規文書のタイトルを指定します。

_pszIconPath_

新規文書として使用したいアイコンのパスとファイル名を指定します。

_pszConfig_

新規文書が使用すべき構成の名前を指定します。

_ptInitialCaret_

初期のカーソル位置を指定します。

_nID_

アクティブ化または一時テキストを閉じたいときの ID を指定します。

_nEncoding_

ファイルのエンコードを指定します。

_nFlags_

下記の中から一つを指定します。

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | nID が０ の場合、一時テキストを開きます。nID が 0 でない場合、存在する一時テキストをアクティブ化します。 |
| TEMP\_INFO\_CLOSE | nID に指定された一時テキストを閉じます。 |
| TEMP\_INFO\_SAVE | nID に指定された一時テキストを保存します。 |
| TEMP\_INFO\_QUIT | nID に指定された一時テキストを保存しないで閉じます。 |
| TEMP\_INFO\_NO\_ID | 一時ファイルを開き、ID を設定しません。このフラグによって開かれた文書は、ユーザーが [ファイル] メニューの [名前を付けて保存] を選択することによりファイルに保存することができます。 |

## バージョン

Version 9.00 以上で利用できます。
