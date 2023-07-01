# ChangeWidth Method (Selection Object)

Changes the width of the selected text.

#### \[JavaScript\]

document.selection. **ChangeWidth**( _nFlags_ \[, _szChars_ \] );

#### \[VBScript\]

document.selection. **ChangeWidth** _nFlags_ \[, _szChars_ \]

## Parameters

_nFlags_

Specifies a combination of the following values: Cannot combine eeWidthFullWidth
and eeWidthHalfWidth together.

|     |     |
| --- | --- |
| eeWidthFullWidth | Converts half-width characters to full-width characters. |
| eeWidthHalfWidth | Converts full-width characters to half-width characters. |
| eeWidthKatakana | Applies conversion to Katakana. |
| eeWidthAlphanumeric | Applies conversion to alphabets and numbers. |
| eeWidthMarks | Applies conversion to marks. |
| eeWidthSpaces | Applies conversion to spaces. |
| eeWidthKanaMarks | Applies conversion to Kana marks. |
| eeWidthAllTypes | Applies conversion to all applicable characters. |
| eeWidthCustom | The szChars parameter specifies which individual characters should be converted. If this value is specified, you must also specify the szChars parameter, and FLAG\_CONVERT\_KATA, FLAG\_CONVERT\_ALPHANUMERIC, FLAG\_CONVERT\_MARK, FLAG\_CONVERT\_SPACE, FLAG\_CONVERT\_KANA\_MARK values are ignored. |
| eeWidthJapaneseYen | Converts U+005C (REVERSE SOLIDUS) to U+FFE5 (FULLWIDTH YEN SIGN), and vice versa. |
| eeWidthKoreanWon | Converts U+005C (REVERSE SOLIDUS) to U+FFE6 (FULLWIDTH WON SIGN), and vice versa. |
| eeWidthRightSingleQuotation | Converts U+0027 (APOSTROPHE) to U+2019 (RIGHT SINGLE QUOTATION MARK), and vice versa. |
| eeWidthRightDoubleQuotation | Converts U+0022 (QUOTATION MARK) to U+201D (RIGHT DOUBLE QUOTATION MARK), and vice versa. |

_szChars_

You can set a combination of individual full-width characters you want to convert if eeWidthCustom is specified. You can omit this parameter if not used.

## Version

Supported on EmEditor Professional Version 4.00 or later.
