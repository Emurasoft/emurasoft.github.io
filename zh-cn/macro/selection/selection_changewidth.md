# ChangeWidth 方法 (Selection ����)

变更所选取的文本的宽度。

#### \[JavaScript\]

document.selection. **ChangeWidth**( _nFlags_ \[, _szChars_ \] );

#### \[VBScript\]

document.selection. **ChangeWidth** _nFlags_ \[, _szChars_ \]

## 参数

_nFlags_

指定一个下列值的组合: eeWidthFullWidth 不能
和 eeWidthHalfWidth 一起使用。

|     |     |
| --- | --- |
| eeWidthFullWidth | 半角字符转换为全角字符。 |
| eeWidthHalfWidth | 全角字符转换为半角字符。 |
| eeWidthKatakana | 转换片假名。 |
| eeWidthAlphanumeric | 转换字母和数字。 |
| eeWidthMarks | 转换标记。 |
| eeWidthSpaces | 转换空格。 |
| eeWidthKanaMarks | 转换假名标记。 |
| eeWidthAllTypes | 转换所有适用的字符。 |
| eeWidthCustom | szChars 参数指定应转换哪些单个字符。如果指定了此值，则还必须指定 szChars 参数，并忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
| eeWidthJapaneseYen | 将 U+005C（反斜线号）转换为 U+FFE5（全角日元标记），反之亦然。 |
| eeWidthKoreanWon | 将 U+005C（反斜线号）转换为 U+FFE6（全角韩元标记），反之亦然。 |
| eeWidthRightSingleQuotation | 将 U+0027（撇号）转换为 U+2019（右单引号），反之亦然。 |
| eeWidthRightDoubleQuotation | 将 U+0022（引号）转换为 U+201D（右双引号），反之亦然。 |

_szChars_

如果指定了 eeWidthCustom，则可以设置要转换的单个全角字符的组合。如果不使用，可以省略此参数。

## 版本

支持 EmEditor 4.00 或之后的版本。
