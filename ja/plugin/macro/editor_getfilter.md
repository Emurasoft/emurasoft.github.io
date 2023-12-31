# Editor\_GetFilter

現在の文書にかけられているフィルターの文字列と設定を取得します。このインライン関数を使うか、または [EE\_GET\_FILTER](../message/ee_get_filter) メッセージを直接送ることができます。

Editor\_GetFilter( HWND hwnd, int iFilter, LPWSTR pszFilter, UINT cchFilter, int\* piColumn, UINT64\* pnFlags, INT\_PTR\* pxBegin, INT\_PTR\* pxEnd );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pszFilter_

フィルター文字列を取得するバッファを指定します。

_cchFilter_

フィルター文字列を取得するバッファのサイズを文字単位で指定します。

_piColumn_

取得するテキストの列のインデックスを格納する整数へのポインタを指定します。行全体から検索する場合、このインデックスは -1 になります。

_pnFlags_

フラグを取得する 64-bit 整数へのポインタを指定します。取得されるフラグは次の値の組み合わせになります。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_ESCAPE | 文字列をエスケープ シーケンスで指定します。 |
| FLAG\_FIND\_LOGICAL\_OR | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
| FLAG\_FIND\_NEGATIVE | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
| FLAG\_FIND\_REG\_EXP | 文字列を正規表現で指定します。 |

_pxBegin_

検索したいテキストの開始位置が論理文字単位で指定されるインデックスを取得する整数へのポインタを指定します。テキストの最後から数えて \*pxEnd で指定する場合には -1
になります。

_pxEnd_

検索したいテキストの終了位置が論理文字単位で指定されるインデックスを取得する整数へのポインタを指定します。最後まで全部を検索する場合には -1
になります。

## 戻り値

iFilter が 0 以上でメッセージが成功すると、戻り値は TRUE になります。iFilter が -1 の場合、戻り値はフィルターの数になります。
