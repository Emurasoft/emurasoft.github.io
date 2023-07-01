# FILTER\_INFO

[EE\_FILTER](../message/ee_filter) メッセージで使用します。この構造体は廃止になりました。新しいプラグインはこの代わりに [FILTER\_INFO\_EX 構造体](filter_info_ex) を使用してください。

typedef struct \_FILTER\_INFO {

UINT     cbSize;

UINT     flags;

int      iColumn;

LPCWSTR  pszFilter;

INT\_PTR  xBegin;

INT\_PTR  xEnd;

} FILTER\_INFO;

## フィールド

_cbSize_

> この構造体のサイズ、sizeof( FILTER\_INFO ) を指定します。

_flags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
> | FLAG\_FIND\_CONTINUE | 次に EE\_FILTER メッセージを呼ぶ際にフィルターをクリアしないことを示します。この EE\_FILTER メッセージの直後には、フィルターが適用されず、次のメッセージまでフィルターの適用を待ちます。このフラグは複数レベルのフィルタを作成する時に使用します。FLAG\_FIND\_KEEP\_PREVIOUS フラグと似ていますが、EE\_FILTER <br> メッセージを呼び出す毎にフィルターが適用されないため、複数のレベルが存在する場合には、FLAG\_FIND\_KEEP\_PREVIOUS より高速に動作します。 |
> | FLAG\_FIND\_ESCAPE | 文字列をエスケープ シーケンスで指定します。 |
> | FLAG\_FIND\_KEEP\_PREVIOUS | この EE\_FILTER メッセージによって既存のフィルターをクリアしないことを示します。このフラグは複数レベルのフィルタを作成する時に使用します。 |
> | FLAG\_FIND\_LOGICAL\_OR | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
> | FLAG\_FIND\_NEGATIVE | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
> | FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
> | FLAG\_FIND\_REG\_EXP | 文字列を正規表現で指定します。 |
> | FLAG\_FIND\_REMOVE\_LAST | 最後に追加されたフィルターのレベルを削除します。 |

_iColumn_

> 検索したい列のインデックスを指定します。-1 を指定すると行全体から検索します。-2 を指定すると xBegin と xEnd
> フィールドによってテキストの開始位置と終了位置を指定します。

_pszFilter_

> 検索する文字列を指定します。

_xBegin_

> 検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて xEnd で指定する場合には -1
> を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。

_xEnd_

> 検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には -1
> を指定します。このフィールドを有効にするには iColumn フィールドに -2 を指定する必要があります。
