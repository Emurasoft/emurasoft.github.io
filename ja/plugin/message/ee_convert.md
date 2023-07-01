# EE\_CONVERT

文字変換を行います。このメッセージを直接送るか、または [Editor\_Convert インライン関数](../macro/editor_convert) を使うことができます。

EE\_CONVERT

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szChars;

## パラメータ

_nFlags_

> 次の値の組み合わせになります。
>
> | 定数 | 説明 |
> | --- | --- |
> | FLAG\_MAKE\_LOWER | 小文字に変換します |
> | FLAG\_MAKE\_UPPER | 大文字に変換します |
> | FLAG\_HAN\_TO\_ZEN | 全角に変換します |
> | FLAG\_ZEN\_TO\_HAN | 半角に変換します |
> | FLAG\_CAPITALIZE | 単語の最初の文字を大文字に変換します |
> | FLAG\_MAKE\_LOWER | 小文字に変換します (ロケール依存) |
> | FLAG\_MAKE\_UPPER | 大文字に変換します (ロケール依存) |
> | FLAG\_CAPITALIZE | 単語の最初の文字を大文字に変換します (ロケール依存) |
> | FLAG\_CONVERT\_SELECT\_ALL | テキスト全部を対象とします。これが指定されていない場合、選択テキストのみを対象とします。 |
> | FLAG\_CONVERT\_KATA | かたかなを対象とします |
> | FLAG\_CONVERT\_ALPHANUMERIC | 英数字を対象とします |
> | FLAG\_CONVERT\_MARK | 記号を対象とします |
> | FLAG\_CONVERT\_SPACE | 空白を対象とします |
> | FLAG\_CONVERT\_KANA\_MARK | かな記号を対象とします |
> | FLAG\_CONVERT\_CUSTOM | FLAG\_HAN\_TO\_ZEN または FLAG\_ZEN\_TO\_HAN が指定されている場合、szChars パラメーターは、変換する個々の文字を指定します。この値を指定する場合は、szChars パラメーターも指定する必要があり、FLAG\_CONVERT\_KATA、FLAG\_CONVERT\_ALPHANUMERIC、FLAG\_CONVERT\_MARK、FLAG\_CONVERT\_SPACE、FLAG\_CONVERT\_KANA\_MARK の値は無視されます。 |
> | FLAG\_JAPANESE\_YEN | U+005C (REVERSE SOLIDUS) を U+FFE5 (FULLWIDTH YEN SIGN) に変換します。逆も同じです。 |
> | FLAG\_KOREAN\_WON | U+005C (REVERSE SOLIDUS) を U+FFE6 (FULLWIDTH WON SIGN) に変換します。逆も同じです。 |
> | FLAG\_RIGHT\_SINGLE\_QUOTATION | U+0027 (APOSTROPHE) を U+2019 (RIGHT SINGLE QUOTATION MARK) に変換します。逆も同じです。 |
> | FLAG\_RIGHT\_DOUBLE\_QUOTATION | U+0022 (QUOTATION MARK) を U+201D (RIGHT DOUBLE QUOTATION MARK) に変換します。逆も同じです。 |

_szChars_

> FLAG\_CONVERT\_CUSTOM が指定されている場合、変換する個々の全角文字の組み合わせを設定できます。使用しない場合は、このパラメーターを NULL に設定します。

## 戻り値

> 成功すると 0 以外を返します。失敗すると 0 を返します。
