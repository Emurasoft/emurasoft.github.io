# PopupMenu 对象

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一个新的项目到菜单末尾。 |
| **[AddPopup](addpopup)** | 添加一个新的子菜单到菜单末尾。 |
| **[GetText](gettext)** | 检索被标识符指定的菜单项目的文本字符串。 |
| **[MsgBox](msgbox)** | 根据对象提供的信息显示对话框，并检索所选按钮、单选按钮或命令链接的标识符。 |
| **[Track](track)** | 显示弹出菜单，检索所选菜单项的标识符。 |

## 示例

#### \[JavaScript\]

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

#### \[VBScript\]

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

## 版本

支持 EmEditor 5.00 或之后的版本。

```{toctree}
:maxdepth: 1
add
addpopup
gettext
msgbox
track
```
