# Windows 컬렉션

Windows 컬렉션은 window 개체의 컬렉션을 제공합니다.

## 속성

|     |     |
| --- | --- |
| **[Count](count)** | 창의 수를 검색합니다. |
| **[Item](item)** | 지정된 인덱스의 창을 위한 window 개체를 검색합니다. |

## 예시

### \[JavaScript\]

```
wnds = new Enumerator( shell.windows );
for( ; !wnds .atEnd(); wnds.moveNext() ){
wnd = wnds.item();
if( wnd.Caption == "Calculator" ){
alert( "Found Calculator window" );
break;
}
}
```

### \[VBScript\]

```
For Each wnd In shell.windows
If wnd.Caption = "Calculator" Then
alert "Found Calculator window"
Exit For
End If
Next
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
