# LOAD\_FILE\_INFO\_EX

[Editor\_LoadFileA](../macro/editor_loadfilea),
[Editor\_LoadFileW](../macro/editor_loadfilew),
[Editor\_InsertFileA](../macro/editor_insertfilea),
[Editor\_InsertFileW](../macro/editor_insertfilew) インライン関数 ( [EE\_LOAD\_FILEA](../message/ee_load_filea),
[EE\_LOAD\_FILEW](../message/ee_load_filew),
[EE\_INSERT\_FILEA](../message/ee_insert_filea),
[EE\_INSERT\_FILEW](../message/ee_insert_filew) メッセージ) で使用します。

```
typedef struct _LOAD_FILE_INFO_EX {
	size_t cbSize;
	UINT nCP;
	BOOL bDetectUnicode;
	BOOL bDetectAll;
	BOOL bDetectCharset;
	BOOL bDetectUTF8;
	UINT nFlags;
} LOAD_FILE_INFO_EX;
```

## フィールド

_cbSize_

sizeof(LOAD\_FILE\_INFO\_EX) を指定します。

_nCP_

開く時に指定するCODEPAGE\_ で始まるコードページを指定します。

| 定数 | 説明 |
| --- | --- |
| CODEPAGE\_CONFIG | 開かれるファイルに関連付けられている設定に指定されているファイル エンコードを使用します。 |
| CODEPAGE\_ANSI | 標準ANSI |
| CODEPAGE\_UNICODE | Unicode little endian |
| CODEPAGE\_UNICODE\_BIGENDIAN | Unicode big endian |
| CODEPAGE\_UTF8 | UTF-8 |
| CODEPAGE\_UTF7 | UTF-7 |
| CODEPAGE\_932 | 日本語 Shift JIS |
| CODEPAGE\_JIS | 日本語 JIS |
| CODEPAGE\_EUC | 日本語 EUC |
| CODEPAGE\_AUTO\_SJIS\_JIS | 日本語 Shift JIS と JIS から自動検出 |
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | 日本語 Shift JIS、JIS、EUC から自動検出 |
| その他 | システムで利用できるコードページが使えます |

_bDetectUnicode_

TRUEなら、Unicodeを検出します。

_bDetectAll_

TRUEなら、すべてのコードページを検出します。

_bDetectCharset_

TRUEなら、HTML/XMLのCharsetを検出します。

_bDetectUTF8_

TRUEなら、UTF-8を検出します。

_nFlags_

次の値の組み合わせで指定します。

| 定数 | 説明 |
| --- | --- |
| LFI\_ALLOW\_ASYNC\_OPEN | ファイルが非同期に開くことを許します。 |
| LFI\_ALLOW\_NEW\_WINDOW | ファイルを新しいウィンドウで開きます。 |
| LFI\_USE\_DISK\_MODE | ファイルを開く際、一時ファイルを使用します。 |
| LFI\_DONT\_USE\_DISK\_MODE | ファイルを開く際、一時ファイルを使用しません。LFI\_USE\_DISK\_MODE も LFI\_DONT\_USE\_DISK\_MODE も指定されていない場合、EmEditor は開こうとするファイルのサイズによって自動的に一時ファイルを使用するかどうかを選択します。 |
| LFI\_DONT\_ADD\_RECENT | 最近使ったファイルにファイル パスを追加しません。 |
