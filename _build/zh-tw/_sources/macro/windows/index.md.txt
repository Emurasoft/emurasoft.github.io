# Windows 集合

Windows 集合提供了視窗對象的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索視窗數目。 |
| **[Item](item)** | 為指定索引的視窗檢索視窗對象。 |

## 示例

#### \[JavaScript\]

wnds = new Enumerator( shell.windows );

for( ; !wnds .atEnd(); wnds.moveNext() ){

wnd = wnds.item();

if( wnd.Caption == "Calculator" ){

alert( "Found Calculator window" );

break;

}

}

#### \[VBScript\]

For Each wnd In shell.windows

If wnd.Caption = "Calculator" Then

alert "Found Calculator window"

Exit For

End If

Next

## 版本

支持 EmEditor 7.00 或之後的版本。

```{toctree}
:maxdepth: 1
count
item
```
