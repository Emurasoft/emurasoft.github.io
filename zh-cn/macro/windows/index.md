# Windows 集合

Windows 集合提供了窗口对象的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索窗口数目。 |
| **[Item](item)** | 为指定索引的窗口检索窗口对象。 |

## 示例

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

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:maxdepth: 1
count
item
```
