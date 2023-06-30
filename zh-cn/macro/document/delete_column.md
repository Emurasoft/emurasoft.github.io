# DeleteColumn 方法 (Document ����)

删除 CSV 模式中指定的列。

#### \[JavaScript\]

document. **DeleteColumn**( _iColumn_, \[ _iColumn2_ \] );

#### \[VBScript\]

document. **DeleteColumn** _iColumn_, \[ _iColumn2_ \]

## 参数

_iColumn1_

指定要删除的第一列。

_iColumn2_

指定要删除的最后一列。如果省略，只有 _iColumn1_ 指定的列会被删除。

## 示例

以下示例会删除第 3 到 5 列。

#### \[JavaScript\]

document.DeleteColumn( 3, 5 );

#### \[VBScript\]

document.DeleteColumn 3, 5

## 版本

支持 EmEditor Professional 21.0 或之后的版本。