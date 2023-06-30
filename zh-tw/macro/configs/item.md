# Item 屬性 (Configs ���X)

為指定索引的組態檢索 [**Config** 對象](../config/index)。

#### \[JavaScript\]

_doc_ = editor.Configs. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.Configs. **Item**( _Index_ )

## 參數

_Index_

把組態索引指定為以 1 為基準的整數。

## 示例

#### \[JavaScript\]

alert( "Name for the first configuration: " + editor.Configs.Item(1).Name );

#### \[VBScript\]

alert "Name for the first configuration: " & editor.Configs.Item(1).Name

## 版本

支持 EmEditor 7.00 或之後的版本。