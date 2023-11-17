# GREP\_INFOA

[Editor\_FindInFilesA インライン関数](../macro/editor_findinfilesa)、 [Editor\_ReplaceInFilesA インライン関数](../macro/editor_replaceinfilesa) ( [EE\_FIND\_IN\_FILESA メッセージ](../message/ee_find_in_filesa)、 [EE\_REPLACE\_IN\_FILESA メッセージ](../message/ee_replace_in_filesa)) で使用します。

```
typedef struct _GREP_INFOA {
	size_t cbSize;
	UINT nCP;
	UINT nFlags;
	LPCSTR pszFind;
	LPCSTR pszReplace;
	LPCSTR pszPath;
	LPCSTR pszBackupPath;
	LPCSTR pszFilesToIgnore;
} GREP_INFOA;
```

## フィールド

_cbSize_

sizeof(GREP\_INFOA) を指定します。

_nCP_

開く時に指定するCODEPAGE\_ で始まるコードページを指定します。

|     |     |
| --- | --- |
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
| CODEPAGE\_DETECT\_UNICODE | Unicodeを検出します。他の値と組み合わせて使用します。 |
| CODEPAGE\_DETECT\_UTF8 | UTF-8を検出します。他の値と組み合わせて使用します。 |
| CODEPAGE\_DETECT\_CHARSET | HTML/XMLのCharsetを検出します。他の値と組み合わせて使用します。 |
| CODEPAGE\_DETECT\_ALL | すべてのコードページを検出します。他の値と組み合わせて使用します。 |

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_ESCAPE | 文字列をエスケープ シーケンスで指定します。FLAG\_FIND\_REG\_EXP と組み合わせて指定できません。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 見つかったファイルのファイル名だけを結果として表示し、検索した文字列を含む行の内容は表示しません。FLAG\_FIND\_LINE\_ONLY または FLAG\_FIND\_MATCHED\_ONLY と組み合わせて指定できません。 |
| FLAG\_FIND\_IGNORE\_FILES | pszFilesToIgnore で指定する名前のファイルまたはフォルダを無視します。 |
| FLAG\_FIND\_LINE\_ONLY | 検索した文字列を含む行の内容だけが結果として表示されます。FLAG\_FIND\_FILENAMES\_ONLY または FLAG\_FIND\_MATCHED\_ONLY と組み合わせて指定できません。 |
| FLAG\_FIND\_MATCHED\_ONLY | 一致した文字列のみが結果として表示されます。FLAG\_FIND\_FILENAMES\_ONLY または FLAG\_FIND\_LINE\_ONLY と組み合わせて指定できません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
| FLAG\_FIND\_RECURSIVE | サブフォルダも検索します。 |
| FLAG\_FIND\_REG\_EXP | 文字列を正規表現で指定します。FLAG\_FIND\_ESCAPE と組み合わせて指定できません。 |
| FLAG\_FIND\_OPEN\_DIRECT | ファイルから検索の結果を一覧としては表示せずに、検索文字列を含むファイルを直接開きます。FLAG\_FIND\_OPEN\_FILTER または FLAG\_FIND\_OUTPUT と組み合わせて指定できません。 |
| FLAG\_FIND\_OPEN\_FILTER | ファイルから検索の結果を一覧としては表示せずに、検索文字列を含むファイルを直接開き、さらにフィルターに検索文字列を設定します。FLAG\_FIND\_OPEN\_DIRECT または FLAG\_FIND\_OUTPUT と組み合わせて指定できません。 |
| FLAG\_FIND\_OUTPUT | ファイルから検索の結果を一覧としてアウトプット バーに表示します。FLAG\_FIND\_OPEN\_DIRECT または FLAG\_FIND\_OPEN\_FILTER と組み合わせて指定できません。 |
| FLAG\_REPLACE\_BACKUP | ファイルから置換の場合、バックアップを保存します。FLAG\_REPLACE\_KEEP\_OPEN と組み合わせて指定できません。 |
| FLAG\_REPLACE\_KEEP\_OPEN | ファイルから置換の場合、変更したファイルを開いたままにします。FLAG\_REPLACE\_BACKUP と組み合わせて指定できません。 |

_pszFind_

検索する文字列を指定します。

_pszReplace_

ファイルから置換の場合、置換後の文字列を指定します。

_pszPath_

検索するパスを指定します。ここには、\\* または ? のワイルド カードを含めて指定することができます。

_pszBackupPath_

ファイルから置換の場合で、 _nFlags_ に FLAG\_REPLACE\_BACKUP を指定した場合、バックアップ先フォルダを指定します。

_pszFilesToIgnore_

_nFlags_ に FLAG\_FIND\_IGNORE\_FILES
を指定した場合、無視するファイルまたはフォルダの名前を指定します。ここには、\\* または ? のワイルド
カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

## バージョン

EmEditor Professional Version 4.02 以上で利用できます。
