# Item 属性

为指定索引的配置检索 [**Config** 对象](../config/index)。

#### \[JavaScript\]

_doc_ = editor.Configs. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.Configs. **Item**( _Index_ )

## 参数

_Index_

把配置索引指定为以 1 为基准的整数。

## 示例

#### \[JavaScript\]

alert( "Name for the first configuration: " + editor.Configs.Item(1).Name );

#### \[VBScript\]

alert "Name for the first configuration: " & editor.Configs.Item(1).Name

## 版本

支持 EmEditor 7.00 或之后的版本。