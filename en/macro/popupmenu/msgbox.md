# MsgBox Method (PopupMenu Object)

Displays the dialog box based on the information provided by the object, and retrieves the identifier of the selected button, radio button, or command link. This method ignores separator items and submenus.

## 

### \[JavaScript\]

```
id = popupmenu.MsgBox( message, message2, flags );
```

### \[VBScript\]

```
id = popupmenu.MsgBox( message, message2, flags )
```

## Parameters

_strMessage_

Specifies a message to be displayed.

_strMessage2_

Optional. Specifies an additional message to be displayed below the first message.

_flags_

Optional. Specifies a combination of the following values. eeCommandLinks and eeRadioButtons cannot be combined.

|     |     |
| --- | --- |
| eeCommandLinks | Indicates that the menu items are to be displayed as command links instead of push buttons. |
| eeRadioButtons | Indicates that the menu items are to be displayed as radio buttons instead of push buttons. |
| eeHideStopMacro | Hides the Stop Macro check box from the dialog box. |
| eeIconStop | A stop-sign icon appears in the dialog box. |
| eeIconExclamation | An exclamation-point icon appears in the dialog box. |
| eeIconInformation | An icon consisting of a lowercase letter i in a circle appears in the dialog box. |

## Examples

### \[JavaScript\]

```
menu = CreatePopupMenu();
menu.Add( "Button 1", 1, eeMenuChecked );
menu.Add( "Button 2", 2 );
result = menu.MsgBox( "Header", "Body", eeIconInformation );
if( result != 0 ) alert( menu.GetText( result ) );
result = menu.MsgBox( "Header", "Body", eeCommandLinks | eeIconExclamation );
if( result != 0 ) alert( menu.GetText( result ) );
result = menu.MsgBox( "Header", "Body", eeRadioButtons | eeIconStop | eeHideStopMacro );
if( result != 0 ) alert( menu.GetText( result ) );
```

### \[VBScript\]

```
Set menu = CreatePopupMenu()
menu.Add "Button 1", 1, eeMenuChecked
menu.Add "Button 2", 2
result = menu.MsgBox( "Header", "Body", eeIconInformation )
If result <> 0 Then alert( menu.GetText( result ) )
result = menu.MsgBox( "Header", "Body", eeCommandLinks Or eeIconExclamation )
If result <> 0 Then alert( menu.GetText( result ) )
result = menu.MsgBox( "Header", "Body", eeRadioButtons Or eeIconStop Or eeHideStopMacro )
If result <> 0 Then alert( menu.GetText( result ) )
```

## Version

Supported on EmEditor Professional Version 20.9 or later.
