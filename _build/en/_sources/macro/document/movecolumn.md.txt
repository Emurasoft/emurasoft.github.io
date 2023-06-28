# MoveColumn 方法

在 CSV 模式下移動或複製指定欄。

#### \[JavaScript\]

document. **MoveColumn**( _iColumn_, _iColumn2_, _iColumnTo_ \[ , _nFlags_ \] );

#### \[VBScript\]

document. **MoveColumn** _iColumn_, _iColumn2_, _iColumnTo_ \[ , _nFlags_ \]

## 參數

_iColumn1_

指定要移動或複製的首欄。

_iColumn2_

指定要移動或複製的最后一欄。

_iColumnTo_

指定要把欄移動或複製到其之前的欄。

_nFlags_

你可以指定以下值之一。如果省略，則會用 eeColumnMove。

| 值 | 含義 |
| --- | --- |
| eeColumnMove | 把從 _iColumn1_ 到 _iColumn2_ 的欄移動到 _iColumnTo_ 的欄之前。 |
| eeColumnCopy | 把從 _iColumn1_ 到 _iColumn2_ 的欄複製到 _iColumnTo_ 的欄之前。 |

## 示例

以下示例將欄 3 移動到最左邊。

#### \[JavaScript\]

document.MoveColumn( 3, 3, 1 );

#### \[VBScript\]

document.MoveColumn 3, 3, 1

## 版本

支持 EmEditor Professional 19.7 或之後的版本。