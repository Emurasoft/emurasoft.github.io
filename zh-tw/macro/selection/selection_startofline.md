# StartOfLine 方法 (Selection ��H)

把游標移動到行首。

#### \[JavaScript\]

document.selection. **StartOfLine**( \[ _bExtend_ \[, _nFlags_ \] \]
);

#### \[VBScript\]

document.selection. **StartOfLine** \[ _bExtend_ \[, _nFlags_ \] \]

## 參數

_bExtend_

可選項。指定是否折疊被移動的文字。預設的值為 false，并且所移動的文字被折疊。

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeLineView | 指定顯示行。 |
| eeLineLogical | 指定邏輯行。 |
| eeLineHomeText | 移動到文字的開始位置，不算空白。 |

## 版本

支持 EmEditor 4.00 或之後的版本。