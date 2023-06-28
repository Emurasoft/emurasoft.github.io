# Editor\_Filter

指定する文字列と設定で文書にフィルターをかけます。このインライン関数を使うか、または [EE\_FILTER](../message/ee_filter) メッセージを直接送ることができます。

Editor\_Filter( HWND hwnd, LPCWSTR szFilter, int iColumn, UINT nFlags,
INT\_PTR xBegin, INT\_PTR xEnd );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szFilter_

> 検索する文字列を指定します。

_iColumn_

> 取得するテキストの列のインデックスを指定します。-1 を指定すると行全体から検索します。

_nFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_BOOKMARKED\_ONLY | ブックマークが設定された行のみ一致します。このフラグは FLAG\_FIND\_UNBOOKMARKED\_ONLY と一緒に指定することはできません。 |
> | FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
> | FLAG\_FIND\_CONTINUE | 次に EE\_FILTER メッセージを呼ぶ際にフィルターをクリアしないことを示します。この EE\_FILTER メッセージの直後には、フィルターが適用されず、次のメッセージまでフィルターの適用を待ちます。このフラグは複数レベルのフィルタを作成する時に使用します。FLAG\_FIND\_KEEP\_PREVIOUS フラグと似ていますが、EE\_FILTER <br> メッセージを呼び出す毎にフィルターが適用されないため、複数のレベルが存在する場合には、FLAG\_FIND\_KEEP\_PREVIOUS より高速に動作します。 |
> | FLAG\_FIND\_CR\_LF | 改行コードが CR+LF の行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
> | FLAG\_FIND\_CR\_ONLY | 改行コードが CR のみの行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
> | FLAG\_FIND\_ESCAPE | 文字列をエスケープ シーケンスで指定します。 |
> | FLAG\_FIND\_FUZZY | あいまい一致を使用します。 |
> | FLAG\_FIND\_KEEP\_PREVIOUS | この EE\_FILTER メッセージによって既存のフィルターをクリアしないことを示します。このフラグは複数レベルのフィルタを作成する時に使用します。 |
> | FLAG\_FIND\_LF\_ONLY | 改行コードが LF のみの行に一致します。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
> | FLAG\_FIND\_LOGICAL\_OR | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
> | FLAG\_FIND\_LINK\_FILE | _szFilter_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になります。 _szFilter_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。 |
> | FLAG\_FIND\_MATCH\_NL | 指定する改行コードに一致します。このフラグは、FLAG\_FIND\_CR\_LF、FLAG\_FIND\_CR\_ONLY、FLAG\_FIND\_LF\_ONLY、または FLAG\_FIND\_NL\_OTHERS と一緒に指定します。 |
> | FLAG\_FIND\_NEGATIVE | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
> | FLAG\_FIND\_NL\_OTHERS | 改行コードが存在しない行に一致します。これらの行には、ファイルの最終行、および改行コード無しで次の行に続く非常に長い行が含まれます。このフラグは、FLAG\_FIND\_MATCH\_NL と一緒に指定する必要があります。 |
> | FLAG\_FIND\_NUMBER\_RANGE | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、FLAG\_FIND\_ESCAPE または FLAG\_FIND\_REG\_EXP と一緒に指定することはできません。 |
> | FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
> | FLAG\_FIND\_REG\_EXP | 文字列を正規表現で指定します。 |
> | FLAG\_FIND\_REMOVE\_LAST | 最後に追加されたフィルターのレベルを削除します。 |
> | FLAG\_FIND\_UNBOOKMARKED\_ONLY | ブックマークが設定されていない行のみ一致します。このフラグは FLAG\_FIND\_BOOKMARKED\_ONLY と一緒に指定することはできません。 |
> | FLAG\_FIND\_WHOLE\_STRING | 文字列全体に一致します。 |

_xBegin_

> 検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて xEnd で指定する場合には -1
> を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。

_xEnd_

> 検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には -1
> を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。

## 戻り値

> 戻り値は、指定する文字列に一致する行数になります。指定文字列が空の場合、戻り値は -1 になります。FLAG\_FIND\_CONTINUE が指定されている場合、戻り値は 0 になります。

## バージョン

> Version 14.7 以上で利用できます。