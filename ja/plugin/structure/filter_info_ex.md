# FILTER\_INFO\_EX

[EE\_FILTER](../message/ee_filter) メッセージと [EE\_GET\_FILTER](../message/ee_get_filter) メッセージで使用します。

```
typedef struct _FILTER_INFO_EX {
	UINT cbSize;
	UINT64 flags;
	int iColumn;
	LPWSTR pszFilter;
	INT_PTR xBegin;
	INT_PTR xEnd;
	UINT cchFilter;
	int nVisibleLinesAbove;
	int nVisibleLinesBelow;
} FILTER_INFO_EX;
```

## フィールド

_cbSize_

この構造体のサイズ、sizeof( FILTER\_INFO\_EX ) を指定します。

_flags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| FLAG\_FIND\_BOOKMARKED\_ONLY | ブックマークが設定された行のみ一致します。このフラグは FLAG\_FIND\_UNBOOKMARKED\_ONLY と一緒に指定することはできません。 |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_CONTINUE | 次に EE\_FILTER メッセージを呼ぶ際にフィルターをクリアしないことを示します。この EE\_FILTER メッセージの直後には、フィルターが適用されず、次のメッセージまでフィルターの適用を待ちます。このフラグは複数レベルのフィルタを作成する時に使用します。FLAG\_FIND\_KEEP\_PREVIOUS フラグと似ていますが、EE\_FILTER メッセージを呼び出す毎にフィルターが適用されないため、複数のレベルが存在する場合には、FLAG\_FIND\_KEEP\_PREVIOUS より高速に動作します。 |
| FLAG\_FIND\_CR\_LF | 改行コードが CR+LF の行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
| FLAG\_FIND\_CR\_ONLY | 改行コードが CR のみの行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
| FLAG\_FIND\_ESCAPE | 文字列をエスケープ シーケンスで指定します。 |
| FLAG\_FIND\_FUZZY | あいまい一致を使用します。 |
| FLAG\_FIND\_KEEP\_PREVIOUS | この EE\_FILTER メッセージによって既存のフィルターをクリアしないことを示します。このフラグは複数レベルのフィルタを作成する時に使用します。 |
| FLAG\_FIND\_LOGICAL\_OR | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
| FLAG\_FIND\_LF\_ONLY | 改行コードが LF のみの行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
| FLAG\_FIND\_LINK\_FILE | _pszFilter_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になります。 _pszFilter_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。 |
| FLAG\_FIND\_MATCH\_NL | 指定する改行コードに一致します。このフラグは、FLAG\_FIND\_CR\_LF、FLAG\_FIND\_CR\_ONLY、FLAG\_FIND\_LF\_ONLY、または FLAG\_FIND\_NL\_OTHERS と一緒に指定します。 |
| FLAG\_FIND\_NEGATIVE | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
| FLAG\_FIND\_NL\_OTHERS | 改行コードが存在しない行に一致します。これらの行には、ファイルの最終行、および改行コード無しで次の行に続く非常に長い行が含まれます。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
| FLAG\_FIND\_NUMBER\_RANGE | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、FLAG\_FIND\_ESCAPE または FLAG\_FIND\_REG\_EXP と一緒に指定することはできません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
| FLAG\_FIND\_REG\_EXP | 文字列を正規表現で指定します。 |
| FLAG\_FIND\_REMOVE\_LAST | 最後に追加されたフィルターのレベルを削除します。 |
| FLAG\_FIND\_UNBOOKMARKED\_ONLY | ブックマークが設定されていない行のみ一致します。このフラグは FLAG\_FIND\_BOOKMARKED\_ONLY と一緒に指定することはできません。 |
| FLAG\_FILTER\_BEGIN | 開始フィルターを指定します。このフラグは FLAG\_FILTER\_END と一緒に指定することはできません。 |
| FLAG\_FILTER\_END | 終了フィルターを指定します。このフラグは FLAG\_FILTER\_BEGIN と一緒に指定することはできません。 |

_iColumn_

検索したい列のインデックスを指定します。-1 を指定すると行全体から検索します。-2 を指定すると xBegin と xEnd
フィールドによってテキストの開始位置と終了位置を指定します。

_pszFilter_

検索する文字列を指定します。

_xBegin_

検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて xEnd で指定する場合には -1
を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。

_xEnd_

検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には -1
を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。

_cchFilter_

取得する文字列を格納するバッファのサイズを文字単位で指定します。

_nVisibleLinesAbove_

一致した行の上に表示する追加の行数を指定します。-1 を指定すると以前に使用されていた値を使用します。

_nVisibleLinesBelow_

一致した行の下に表示する追加の行数を指定します。-1 を指定すると以前に使用されていた値を使用します。
