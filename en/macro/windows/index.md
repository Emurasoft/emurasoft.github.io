# Windows Collection

Windows collection provides a collection of window objects.

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of windows. |
| **[Item](item)** | Retrieves the window object for the window of the specified index. |

## Examples

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

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
