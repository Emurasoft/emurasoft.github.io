# EE\_INSERT\_STRINGA

カーソル位置にANSI文字列を挿入します。このメッセージを直接送るか、または
[Editor\_InsertStringA インライン関数](../macro/editor_insertstringa)、 [Editor\_InsertA インライン関数](../macro/editor_inserta)、または [Editor\_OverwriteA インライン関数](../macro/editor_overwritea) を使うことができます。

```
EE_INSERT_STRINGA
wParam = nInsertType;
lParam = (LPARAM) (LPCSTR) szString;
```

## パラメータ

_nInsertType_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| OVERWRITE\_PER\_PROP | プロパティで指定された方法で挿入または上書きします。 |
| OVERWRITE\_INSERT | 常に挿入し、既存の文字列に上書きしません。 |
| OVERWRITE\_OVERWRITE | 常に既存の文字列に上書きします。 |
| KEEP\_SOURCE\_RETURN\_TYPE | szString パラメータで指定されている改行コード (CR のみ、LF のみ、または CR+LF) を保持します。 |
| KEEP\_DEST\_RETURN\_TYPE | 挿入先のカーソル位置の改行コードを保持します。 |

_szString_

挿入する文字列を指定します。

## 戻り値

戻り値は利用されません。

## バージョン

KEEP\_SOURCE\_RETURN\_TYPE と KEEP\_DEST\_RETURN\_TYPE は、EmEditor Version 7.00 以上で利用できます。
