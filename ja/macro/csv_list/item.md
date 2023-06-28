# Item プロパティ

指定したインデックスの [Csv オブジェクト](../csv/index) を取得します。

#### \[JavaScript\]

_doc_ = editor.CsvList. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.CsvList. **Item**( _Index_ )

## パラメータ

_Index_

Csv オブジェクトのインデックスを 1 から始まる整数として指定します。

## 例

#### \[JavaScript\]

alert( "Name for the first Csv object: " + editor.CsvList.Item(1).Name );

#### \[VBScript\]

alert "Name for the first Csv object: " & editor.CsvList.Item(1).Name

## バージョン

EmEditor Professional Version 19.4 以上で利用できます。