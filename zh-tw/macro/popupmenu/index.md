# PopupMenu 對象

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一個新的項目到功能表末尾。 |
| **[AddPopup](addpopup)** | 添加一個新的子功能表到功能表末尾。 |
| **[GetText](gettext)** | 檢索被識別項指定的功能表項目的文字字串。 |
| **[MsgBox](msgbox)** | 根據對象提供的信息顯示對話方塊，並檢索所選按鈕、選項按鈕或命令連結的識別項。 |
| **[Track](track)** | 顯示快顯功能表，檢索所選功能表項的識別項。 |

## 範例

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

## 版本

支持 EmEditor 5.00 或之後的版本。


```{toctree}
:maxdepth: 1
add
addpopup
gettext
msgbox
track
```
