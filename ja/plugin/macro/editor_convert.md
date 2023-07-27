# Editor\_Convert

文字変換を行います。このインライン関数を使うか、または [EE\_CONVERT](../message/ee_convert)
または [EE\_CONVERT\_EX](../message/ee_convert_ex)
メッセージを直接送ることができます。

Editor\_Convert( HWND hwnd, UINT nFlags, LPCWSTR szChars = NULL, LPCWSTR pszSeparator = NULL, UINT nSortFlags = 0, LPCWSTR pszLocale = NULL );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

次の値の組み合わせになります。

| 定数 | 説明 |
| --- | --- |
| FLAG\_MAKE\_LOWER | 小文字に変換します |
| FLAG\_MAKE\_UPPER | 大文字に変換します |
| FLAG\_HAN\_TO\_ZEN | 全角に変換します |
| FLAG\_ZEN\_TO\_HAN | 半角に変換します |
| FLAG\_CAPITALIZE | 単語の最初の文字を大文字に変換します |
| FLAG\_MAKE\_LOWER | 小文字に変換します (ロケール依存) |
| FLAG\_MAKE\_UPPER | 大文字に変換します (ロケール依存) |
| FLAG\_CAPITALIZE | 単語の最初の文字を大文字に変換します (ロケール依存) |
| FLAG\_CONVERT\_SELECT\_ALL | テキスト全部を対象とします。これが指定されていない場合、選択テキストのみを対象とします。 |
| FLAG\_CONVERT\_KATA | かたかなを対象とします |
| FLAG\_CONVERT\_ALPHANUMERIC | 英数字を対象とします |
| FLAG\_CONVERT\_MARK | 記号を対象とします |
| FLAG\_CONVERT\_SPACE | 空白を対象とします |
| FLAG\_CONVERT\_KANA\_MARK | かな記号を対象とします |
| FLAG\_CONVERT\_CUSTOM | FLAG\_HAN\_TO\_ZEN または FLAG\_ZEN\_TO\_HAN が指定されている場合、szChars パラメーターは、変換する個々の文字を指定します。この値を指定する場合は、szChars パラメーターも指定する必要があり、FLAG\_CONVERT\_KATA、FLAG\_CONVERT\_ALPHANUMERIC、FLAG\_CONVERT\_MARK、FLAG\_CONVERT\_SPACE、FLAG\_CONVERT\_KANA\_MARK の値は無視されます。 |
| FLAG\_JAPANESE\_YEN | U+005C (REVERSE SOLIDUS) を U+FFE5 (FULLWIDTH YEN SIGN) に変換します。逆も同じです。 |
| FLAG\_KOREAN\_WON | U+005C (REVERSE SOLIDUS) を U+FFE6 (FULLWIDTH WON SIGN) に変換します。逆も同じです。 |
| FLAG\_RIGHT\_SINGLE\_QUOTATION | U+0027 (APOSTROPHE) を U+2019 (RIGHT SINGLE QUOTATION MARK) に変換します。逆も同じです。 |
| FLAG\_RIGHT\_DOUBLE\_QUOTATION | U+0022 (QUOTATION MARK) を U+201D (RIGHT DOUBLE QUOTATION MARK) に変換します。逆も同じです。 |

_szChars_

FLAG\_CONVERT\_CUSTOM が指定されている場合、変換する個々の全角文字の組み合わせを設定できます。使用しない場合は、このパラメーターを NULL に設定します。

_pszSeparator_

列を分割する際に使用する区切り文字列を指定します。

_nSortFlags_

次の値の組み合わせを指定します。分割文字列を並べ替えるには SORT\_ENABLED を指定する必要があり、他のフラグと組み合わせて並べ替えの動作を指定します。重複した分割文字列を削除するには SORT\_DELETE\_DUPLICATE を指定する必要があります。

|     |     |
| --- | --- |
| NORM\_IGNORECASE | 大文字と小文字を区別しないで並べ替えます。 |
| NORM\_IGNOREKANATYPE | ひらがなとカタカナを区別しないで並べ替えます。 |
| NORM\_IGNORENONSPACE | 場所を取らない文字を区別しないで並べ替えます。 |
| NORM\_IGNORESYMBOLS | 記号を無視して並べ替えます。 |
| NORM\_IGNOREWIDTH | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
| SORT\_BINARY\_COMPARISON | ロケールを無視して、高速にバイナリ比較を行います。 |
| SORT\_DATE | 日付と時刻で並べ替えます。 |
| SORT\_DELETE\_DUPLICATE | 重複した分割文字列を削除します。 |
| SORT\_DIGITSASNUMBERS | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
| SORT\_ENABLED | 分割文字列を並べ替えます。 |
| SORT\_IGNORE\_PREFIX | 数字を並べ替える際、先頭の数字以外の文字は無視されます。 |
| SORT\_INSPECT\_NOT\_SEL\_ONLY | 箱型選択または複数選択が存在する時でも、行全体を調べます。 |
| SORT\_IPV4 | IPv4 アドレスを並べ替えます。 |
| SORT\_IPV6 | IPv6 アドレスを並べ替えます。 |
| SORT\_LENGTH | 文字数で並べ替えます。 |
| SORT\_LENGTH\_VIEW | \[短い文字列から長い文字列へ並べ替え\] コマンドまたは \[長い文字列から短い文字列へ並べ替え\] コマンドを使用時、全角文字が2文字として扱われます。 |
| SORT\_NUM | 数字を並べ替えます。 |
| SORT\_GROUP\_IDENTICAL | 出現頻度で並べ替える時、同じ文字列をグループ化します。SORT\_OCCURRENCE と共に指定する必要があります。 |
| SORT\_OCCURRENCE | 出現頻度で並べ替えます。 |
| SORT\_RANDOM | ランダムに並べ替えます。 |
| SORT\_REVERSE | 逆順に並べ替えます。 |
| SORT\_STABLE | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
| SORT\_STRINGSORT | 句読点が記号と同様に扱われます。 |
| SORT\_TEXT | テキストを並べ替えます。 |
| SORT\_WORDS | 単語数で並べ替えます。 |

_pszLocale_

並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。
