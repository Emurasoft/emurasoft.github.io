# Add Method

Adds a new item to the end of the menu.

#### \[JavaScript\]

popupmenu. **Add**( _strText_, _id_, _flags_ );

#### \[VBScript\]

popupmenu. **Add** _strText_, _id_, _flags_

## Parameters

_strText_

Specifies text to display. If eeMenuSeparator is set in the _flags_ parameter, an empty string must be specified.

_id_

Specifies the identifier of the new menu item. The Track Method uses this identifier as the return value. If eeMenuSeparator is set in the _flags_ parameter, 0 must be specified.

_flags_

Specifies status of the item. The following flags can be specified.

|     |     |
| --- | --- |
| eeMenuChecked | Places a check mark next to the menu item. |
| eeMenuGrayed | Disables the menu item and grays it so that it cannot be selected. |
| eeMenuSeparator | Draws a horizontal dividing line. This flag cannot be combined with others. |

## Version

Supported on EmEditor Professional Version 5.00 or later.