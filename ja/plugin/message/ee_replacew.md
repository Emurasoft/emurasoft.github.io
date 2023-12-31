# EE\_REPLACEW

Unicode文字列を置換します。このメッセージは使用されなくなります。新しいプラグインは、 [EE\_FIND\_REPLACE メッセージ](ee_find_replace) を使用してください。このメッセージを直接送るか、または [Editor\_ReplaceW インライン関数](../macro/editor_replacew) を使うことができます。

```
EE_REPLACEW
wParam = (WPARAM) (UINT) nFlags;
lParam = (LPARAM) (LPCWSTR) szFindReplace;
```

## パラメータ

_nFlags_

次の値の組み合わせになります。

| 定数 | 説明 |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別します。 |
| FLAG\_FIND\_CLOSE | 終了後、ダイアログ ボックスを閉じます。 |
| FLAG\_FIND\_ESCAPE | エスケープ シーケンスを使用します。 |
| FLAG\_FIND\_NO\_PROMPT | 検索する文字列が見つからなくてもプロンプト ダイアログ ボックスを表示しません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみ選択します。 |
| FLAG\_FIND\_REG\_EXP | 正規表現を使って検索します。 |
| FLAG\_FIND\_SAVE\_HISTORY | 次の検索用に、検索文字列を保存します。 |
| FLAG\_REPLACE\_ALL | すべて置換します。 |
| FLAG\_REPLACE\_SEL\_ONLY | すべて置換の場合に選択範囲のテキストのみを対象とします。FLAG\_REPLACE\_ALL とともに指定する必要があります。 |

_szFindReplace_

検索する文字列と置換後の文字列を指定します。検索する文字列、置換後の文字列の順に指定し、検索する文字列と置換後の文字列の間、置換後の文字列の後にヌル文字
('\\0') を指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。
