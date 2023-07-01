# PopupMenu オブジェクト

## メソッド

|     |     |
| --- | --- |
| [Add](add) | メニューの項目を追加します。 |
| [AddPopup](addpopup) | サブ メニューを追加します。 |
| [GetText](gettext) | 指定する ID に対するテキストを取得します。 |
| [MsgBox](msgbox) | オブジェクトにより提供された情報をもとにダイアログ ボックスを表示して、選択されたボタン、ラジオ ボタン、またはコマンド リンクの ID を返します。 |
| [Track](track) | ポップアップ メニューを表示して、選択されたメニュー項目の ID を返します。 |

## 例

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

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。


```{toctree}
:maxdepth: 1
add
addpopup
gettext
msgbox
track
```
