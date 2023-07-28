# CellMode 属性 (Document 对象)

设置或检索一个标志来显示选择模式是否是单元格选择模式。

## 

### \[JavaScript\]

```
b = document.CellMode;
document.CellMode = b;
```

### \[VBScript\]

```
b = document.CellMode
document.CellMode = b
```

## 范例

### \[JavaScript\]

```
if( document.CellMode )  alert( "单元格选择模式." );
else  alert( "不是单元格选择模式." );
```

### \[VBScript\]

```
If document.CellMode Then
alert( "单元格选择模式." )
Else
alert( "不是单元格选择模式." )
End If
```

## 版本

支持 EmEditor 15.8 或之后的版本。
