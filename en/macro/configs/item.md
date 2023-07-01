# Item Property (Configs Collection)

Retrieves the [**Config** object](../config/index) for the configuration of the specified index.

#### \[JavaScript\]

_doc_ = editor.Configs. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.Configs. **Item**( _Index_ )

## Parameters

_Index_

Specifies the index of the configuration as a one-based integer.

## Examples

#### \[JavaScript\]

alert( "Name for the first configuration: " + editor.Configs.Item(1).Name );

#### \[VBScript\]

alert "Name for the first configuration: " & editor.Configs.Item(1).Name

## Version

Supported on EmEditor Professional Version 7.00 or later.
