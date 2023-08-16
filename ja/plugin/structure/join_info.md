# JOIN\_INFO

[EE\_JOIN](../message/ee_join) メッセージで使用します。

```
typedef struct _JOIN_INFO {
	UINT cbSize;
	UINT flags;
	LPCWSTR pszDocument1;
	LPCWSTR pszDocument2;
	LPCWSTR pszColumn1;
	LPCWSTR pszColumn2;
	LPCWSTR pszSelect;
	UINT iDocument3;
} JOIN_INFO;
```

## フィールド

_cbSize_

この構造体のサイズ、sizeof( JOIN\_INFO ) を指定します。

_flags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| JOIN\_FLAG\_UNIQUE\_KEY\_1 | 第1文書の指定した列には一意キーが含まれます。 |
| JOIN\_FLAG\_UNIQUE\_KEY\_2 | 第2文書の指定した列には一意キーが含まれます。 |
| JOIN\_FLAG\_INCLUDE\_ALL\_1 | 第1文書のすべての行が出力に含まれます。第1文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
| JOIN\_FLAG\_INCLUDE\_ALL\_2 | 第2文書のすべての行が出力に含まれます。第2文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
| JOIN\_FLAG\_MATCH\_CASE | 大文字と小文字を区別します。 |
| JOIN\_FLAG\_SIMPLE\_JOIN | キーを使用しないで、単純に結合します。これを指定した場合、 _pszColumn1_ と _pszColumn2_ パラメータは無視されます。 |
| JOIN\_FLAG\_IGNORE\_HEADINGS\_1 | 第1文書のヘディングを無視します。第1文書のヘディングは、結合された文書に残ります。 |
| JOIN\_FLAG\_IGNORE\_HEADINGS\_2 | 第2文書のヘディングを無視します。 |
| JOIN\_FLAG\_CONTAIN | Key1 は Key2 を含みます。 |
| JOIN\_FLAG\_START\_WITH | Key1 は Key2 から始まります。 |
| JOIN\_FLAG\_END\_WITH | Key1 は Key2 で終わります。 |
| JOIN\_FLAG\_MATCH\_SPLIT\_BOTH | 両方の分割文字列が一致します。 |
| JOIN\_FLAG\_MATCH\_SPLIT\_ONE | Key1 は 分割した Key2 に一致します。 |
| JOIN\_FLAG\_FUZZY | あいまい一致を使用します。このフラグは、JOIN\_FLAG\_END\_WITH、JOIN\_FLAG\_MATCH\_SPLIT\_BOTH、または JOIN\_FLAG\_MATCH\_SPLIT\_ONE と共に指定することはできません。このフラグは動作を遅くします。 |
| JOIN\_FLAG\_SWAP | JOIN\_FLAG\_CONTAIN、JOIN\_FLAG\_START\_WITH、または JOIN\_FLAG\_END\_WITH と共に指定されている場合、Key1 と Key2 を入れ替えます。 |

_pszDocument1_

第1文書を特定する文字列を指定します。この値は、ファイル名、完全パスの付いたファイル名、またはコロン (:) で始まる現在のグループ内の文書のインデックスになります。例えば、"filename.csv"、"C:\\data\\filename.csv"、または ":2" と指定することができます。

_pszColumn1_

第1文書のキー列を特定する文字列を指定します。この値は、列の最初の行、またはコロン (:) で始まる列のインデックスになります。例えば、"first\_name"、":5" と指定することができます。

_pszDocument2_

第2文書を特定する文字列を指定します。この値のフォーマットは strDocument1 と同じです。

_pszColumn2_

第2文書のキー列を特定する文字列を指定します。この値のフォーマットは strColumn1 と同じです。

_pszSelect_

出力文書にどの列を選択するかを示す文字列を指定します。例えば、"file1.csv>column1,file2.csv>column2" と指定することができます。前の列と連結するには「,」の代わりに「+」を、最初の空でない値を使用するには「,」の代わりに「\|」を使用します。

_iDocument3_

関数が戻ると、このフィールドは出力文書のインデックスが代入されます。

## バージョン

Version 14.8 以上で利用できます。
