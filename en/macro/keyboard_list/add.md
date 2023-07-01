# Add Method (KeyboardList Collection)

Adds an item.

#### \[JavaScript\]

list. **Add**( _nKey_, _nFlags_, _nCommand_ );

#### \[VBScript\]

list. **Add** _nKey_, _nFlags_, _nCommand_

## Parameters

_nKey_

Specifies the key of the item to add.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeVirtualKey | Specifies the Key member of the object is a virtual-key code. If this flag is not specified, the Key member of the object is assumed to specify a character code. |
| eeShift | Specifies the SHIFT key must be held down when the accelerator key is pressed. |
| eeCtrl | Specifies the CTRL key must be held down when the accelerator key is pressed. |
| eeAlt | Specifies the ALT key must be held down when the accelerator key is pressed. |

_nCommand_

Specifies the command ID of the item to add.

## Version

Supported on EmEditor Professional Version 7.00 or later.
