# ChangeWidth 方法

變更所選取的文字的寬度。

#### \[JavaScript\]

document.selection. **ChangeWidth**( _nFlags_ \[, _szChars_ \] );

#### \[VBScript\]

document.selection. **ChangeWidth** _nFlags_ \[, _szChars_ \]

## 參數

_nFlags_

指定一個下列值的組合: eeWidthFullWidth 不能
和 eeWidthHalfWidth 一起使用。

|     |     |
| --- | --- |
| eeWidthFullWidth | 半形字元轉換為全形字元。 |
| eeWidthHalfWidth | 全形字元轉換為半形字元。 |
| eeWidthKatakana | 轉換片假名。 |
| eeWidthAlphanumeric | 轉換字母和數字。 |
| eeWidthMarks | 轉換標記。 |
| eeWidthSpaces | 轉換空白。 |
| eeWidthKanaMarks | 轉換假名標記。 |
| eeWidthAllTypes | 轉換所有適用的字元。 |
| eeWidthCustom | szChars 參數指定應轉換哪些單個字元。如果指定了此值，則還必須指定 szChars 參數，並忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
| eeWidthJapaneseYen | 將 U+005C（反斜線）轉換為 U+FFE5（全形日幣標記），反之亦然。 |
| eeWidthKoreanWon | 將 U+005C（反斜線）轉換為 U+FFE6（全形韓幣標記），反之亦然。 |
| eeWidthRightSingleQuotation | 將 U+0027（縮寫符號）轉換為 U+2019（右單引號），反之亦然。 |
| eeWidthRightDoubleQuotation | 將 U+0022（引號）轉換為 U+201D（右雙引號），反之亦然。 |

_szChars_

如果指定了 eeWidthCustom，則可以設定要轉換的單個全形字元的組合。如果不使用，可以省略此參數。

## 版本

支持 EmEditor 4.00 或之後的版本。