# ChangeWidth メソッド ()

半角文字と全角文字を変換します。

## 

### \[JavaScript\]

```
document.selection.ChangeWidth( nFlags [, szChars ] );
```

### \[VBScript\]

```
document.selection.ChangeWidth nFlags [, szChars ]
```

## パラメータ

_nFlags_

次の組み合わせになります。eeWidthFullWidth と eeWidthHalfWidth は、同時に指定することはできません。

|     |     |
| --- | --- |
| eeWidthFullWidth | 半角文字を全角文字に変換します。 |
| eeWidthHalfWidth | 全角文字を半角文字に変換します。 |
| eeWidthKatakana | カタカナを変換の対象とします。 |
| eeWidthAlphanumeric | 欧文文字と数字を変換の対象とします。 |
| eeWidthMarks | 記号を変換の対象とします。 |
| eeWidthSpaces | 空白文字を変換の対象とします。 |
| eeWidthKanaMarks | かな記号を変換の対象とします。 |
| eeWidthAllTypes | すべての種類の文字を変換の対象とします。 |
| eeWidthCustom | szChars パラメーターは、変換する個々の文字を指定します。この値を指定する場合は、szChars パラメーターも指定する必要があり、FLAG\_CONVERT\_KATA、FLAG\_CONVERT\_ALPHANUMERIC、FLAG\_CONVERT\_MARK、FLAG\_CONVERT\_SPACE、FLAG\_CONVERT\_KANA\_MARK の値は無視されます。 |
| eeWidthJapaneseYen | U+005C (REVERSE SOLIDUS) を U+FFE5 (FULLWIDTH YEN SIGN) に変換します。逆も同じです。 |
| eeWidthKoreanWon | U+005C (REVERSE SOLIDUS) を U+FFE6 (FULLWIDTH WON SIGN) に変換します。逆も同じです。 |
| eeWidthRightSingleQuotation | U+0027 (APOSTROPHE) を U+2019 (RIGHT SINGLE QUOTATION MARK) に変換します。逆も同じです。 |
| eeWidthRightDoubleQuotation | U+0022 (QUOTATION MARK) を U+201D (RIGHT DOUBLE QUOTATION MARK) に変換します。逆も同じです。 |

_szChars_

eeWidthCustom が指定されている場合、変換する個々の全角文字の組み合わせを設定できます。使用しない場合は、このパラメーターを省略できます。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
