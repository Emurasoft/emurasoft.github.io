# HideQuotes 属性 (Document 对象)

检索或设置一个标志，该标志指示在 CSV 单元格选择模式下是否启用了“隐藏引号”视图。

## 

### \[JavaScript\]

```
b = document.HideQuotes;
document.HideQuotes = b;
```

### \[VBScript\]

```
b = document.HideQuotes
document.HideQuotes = b
```

## 示例

### \[JavaScript\]

```
if( document.HideQuotes )  alert( "Unquoted/Unescaped View." );
else  alert( "Not Unquoted/Unescaped View." );
```

### \[VBScript\]

```
If document.HideQuotes Then
alert( "Unquoted/Unescaped View." )
Else
alert( "Not Unquoted/Unescaped View." )
End If
```

## 版本

支持 EmEditor 20.7 或之后的版本。
