# PopupMenu Object

## Methods

|     |     |
| --- | --- |
|[Add](add) | Adds a new item to the end of the menu. |
|[AddPopup](addpopup) | Adds a new submenu to the end of the menu. |
|[GetText](gettext) | Retrieves the text string of the menu item specified by the identifier. |
|[MsgBox](msgbox) | Displays the dialog box based on the information provided by the object, and retrieves the identifier of the selected button, radio button, or command link. |
|[Track](track) | Displays the popup menu, and retrieves the identifier of the selected menu item. |

## Examples

### \[JavaScript\]

```
menu = CreatePopupMenu();
submenu = CreatePopupMenu();
menu.Add( "menu 1", 1 );
menu.Add( "menu 2", 2, eeMenuGrayed );
menu.Add( "", 0, eeMenuSeparator );
submenu.Add( "menu 11", 11 );
submenu.Add( "menu 12", 12 );
menu.AddPopup( "more", submenu );
result = menu.Track( 0 );
if( result != 0 ) {
alert( menu.GetText( result ) );
}
```

### \[VBScript\]

```
Set menu = CreatePopupMenu
Set submenu = CreatePopupMenu
menu.Add "menu 1", 1
menu.Add "menu 2", 2, eeMenuGrayed
menu.Add "", 0, eeMenuSeparator
submenu.Add "menu 11", 11
submenu.Add "menu 12", 12
menu.AddPopup "more", submenu
result = menu.Track( 0 )
If result <> 0 Then
alert menu.GetText( result )
End If
```

## Version

Supported on EmEditor Professional Version 5.00 or later.


```{toctree}
:maxdepth: 1
add
addpopup
gettext
msgbox
track
```
