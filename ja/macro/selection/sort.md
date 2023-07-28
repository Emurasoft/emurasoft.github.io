# Sort メソッド (Selection オブジェクト)

選択範囲の分割文字列を並べ替え、または重複した分割文字列を削除します。

## 

### \[JavaScript\]

```
document.selection.Sort( strSeparator, strSortType, nFlags, strLocale );
```

### \[VBScript\]

```
document.selection.Sort strSeparator, strSortType, nFlags, strLocale
```

## 引数

_strSeparator_

列を分割する際に使用する区切り文字列を指定します。このパラメータは空にすることができません。

_strSortType_

フラグを指定する文字列を指定します。省略すると、並べ替えは行われません。フォーマットは以下の通りです。

構文:

option (+/-)

option: 以下のテーブルから並べ替えオプションを選択します。

|     |     |
| --- | --- |
| A | テキストを並べ替えます。 |
| D | 日付と時刻で並べ替えます。 |
| I | IPv4 アドレスを並べ替えます。 |
| P | IPv6 アドレスを並べ替えます。 |
| L | 文字数で並べ替えます。 |
| N | 数字を並べ替えます。 |
| O | 出現頻度で並べ替えます。 |
| V | 逆順に並べ替えます。 |
| W | 単語数で並べ替えます。 |

(+/-): 以下のテーブルから並べ替えオプションを選択します。

|     |     |
| --- | --- |
| + | 昇順。 |
| - | 降順。 |

例:

|     |     |
| --- | --- |
| A+ | テキストを昇順で並べ替えます。 |
| N- | 数字を降順で並べ替えます。 |

_nFlags_

次の値の組み合わせを指定します。分割後に重複文字列を削除するには、eeRemoveDuplicates を指定する必要があります。その他のフラグは、 _strSortType_ に空でない文字列を指定した場合だけ、指定できます。このパラメータは省略できます。

|     |     |
| --- | --- |
| eeDontDiscardExtra | nLimit が 0 でない時、余分な文字列を破棄しません。 |
| eeRemoveDuplicates | 重複文字列を削除します。 |
| eeSortBinaryComparison | ロケールを無視して、高速にバイナリ比較を行います。 |
| eeSortDigitsAsNumbers | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
| eeSortGroupIdentical | 出現頻度で並べ替える時、同じ文字列をグループ化します。 |
| eeSortIgnoreCase | 大文字と小文字を区別しないで並べ替えます。 |
| eeSortIgnoreKanaType | ひらがなとカタカナを区別しないで並べ替えます。 |
| eeSortIgnoreNonSpace | 場所を取らない文字を区別しないで並べ替えます。 |
| eeSortIgnoreSymbols | 記号を無視して並べ替えます。 |
| eeSortIgnoreWidth | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
| eeSortIgnorePrefix | 数字を並べ替える際、先頭の数字以外の文字は無視されます。 |
| eeSortLengthView | \[短い文字列から長い文字列へ並べ替え\] コマンドまたは \[長い文字列から短い文字列へ並べ替え\] コマンドを使用時、全角文字が2文字として扱われます。 |
| eeSortStable | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
| eeSortStringSort | 句読点が記号と同様に扱われます。 |

_strLocale_

並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。
