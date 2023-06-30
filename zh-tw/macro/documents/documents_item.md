# Item 屬性 (Documents ���X)

為指定索引的文檔檢索文檔對象。

#### \[JavaScript\]

_doc_ = editor.Documents. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.Documents. **Item**( _Index_ )

## 參數

_Index_

指定以 1 為基準的整數為文檔的索引。

## 示例

#### \[JavaScript\]

alert( "Full Name for the first document: " + editor.Documents.Item(1).FullName );

#### \[VBScript\]

alert "Full Name for the first document: " & editor.Documents.Item(1).FullName

## 版本

支持 EmEditor 5.00 或之後的版本。