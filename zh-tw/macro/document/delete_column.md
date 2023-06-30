# DeleteColumn 方法 (Document ��H)

刪除 CSV 模式中指定的欄。

#### \[JavaScript\]

document. **DeleteColumn**( _iColumn_, \[ _iColumn2_ \] );

#### \[VBScript\]

document. **DeleteColumn** _iColumn_, \[ _iColumn2_ \]

## 參數

_iColumn1_

指定要刪除的第一欄。

_iColumn2_

指定要刪除的最後一欄。如果省略，只有 _iColumn1_ 指定的欄會被刪除。

## 範例

以下範例會刪除第 3 到 5 欄。

#### \[JavaScript\]

document.DeleteColumn( 3, 5 );

#### \[VBScript\]

document.DeleteColumn 3, 5

## 版本

支持 EmEditor Professional 21.0 或之後的版本。