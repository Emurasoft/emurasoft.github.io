# PopupMenu 개체

## 메서드

|     |     |
| --- | --- |
| **[Add](add)** | 메뉴의 마지막에 새로운 항목을 추가합니다. |
| **[AddPopup](addpopup)** | 메뉴의 마지막에 새로운 하위 메뉴를 추가합니다. |
| **[GetText](gettext)** | 식별자에 의해 지정된 메뉴 항목의 텍스트 문자열을 검색합니다. |
| **[Track](track)** | 팝업 메뉴를 표시합니다. |

## 예시

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

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.

```{toctree}
:maxdepth: 1
add
addpopup
gettext
track
```
