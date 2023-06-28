# COLUMN\_STRUCT

[Editor\_GetColumn](../macro/editor_getcolumn) インライン関数 ( [EE\_GET\_COLUMN](../message/ee_get_column) メッセージ) または [Editor\_SetColumn](../macro/editor_setcolumn) インライン関数 ( [EE\_SET\_COLUMN](../message/ee_set_column) メッセージ) で使用します。

typedef struct \_COLUMN\_STRUCT {

UINT cbSize;

int iColumn;

UINT\_PTR yLineTop;

UINT\_PTR yLines;

LPWSTR pBuf

UINT\_PTR cchBuf;

LPCWSTR pszDelimiter;

UINT flags;

HGLOBAL hGlobalData;

} COLUMN\_STRUCT;

## フィールド

_cbSize_

> この構造体のサイズをバイト数で指定します。

_iColumn_

> 列のインデックスを指定します。

_yLineTop_

> 設定する最初の行の行番号を指定します。0 を指定すると、最初の行を指定します。

_yLines_

> 行数を制限として指定します。0 を指定すると、制限は指定されません。

_pBuf_

> Editor\_SetColumn インライン関数 (EE\_SET\_COLUMN メッセージ) で使用する場合、設定する文字列を指定します。文字列は、 _pszDelimiter_ で指定される区切り文字で区切ることができます。Editor\_GetColumn インライン関数 (EE\_GET\_COLUMN メッセージ) で使用する場合、文字列を取得するバッファを指定します。

_cchBuf_

> Editor\_GetColumn インライン関数 (EE\_GET\_COLUMN メッセージ) で使用する場合、バッファのサイズを文字単位で指定します。

_pszDelimiter_

> _pBuf_ で指定された文字列を区切る区切り文字列を指定します。これが空の場合、列のすべてのセルで同じ文字列が使用されます。

_flags_

> 次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 文字列に区切り文字、改行、引用符が含まれていないかを確認し、必要なら自動的にエスケープを行い、引用符を追加します。 |
> | DONT\_QUOTE | 上の処理を行いません。 |
> | ALWAYS\_QUOTE | 常に引用符を追加します。 |
> | USE\_HGLOBAL | Editor\_GetColumn インライン関数 (EE\_GET\_COLUMN メッセージ) で使用する場合、hGlobalData フィールドが新規に割り当てられたグローバル メモリを受け取ることを指定します。このフラグを使用する場合、pBuf と cchBuf フィールドは 0 でなければなりません。 |

_hGlobalData_

> Editor\_GetColumn インライン関数 (EE\_GET\_COLUMN メッセージ) で使用する場合、新規に割り当てられたグローバル メモリ オブジェクトへのハンドルを受け取る変数を指定します。呼び出し側はこのメモリ オブジェクトを GlobalFree 関数を用いて解放する必要があります。