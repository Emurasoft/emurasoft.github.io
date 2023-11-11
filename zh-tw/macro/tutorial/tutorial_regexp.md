# 使用規則運算式 (教程)

要使用規則運算式，請用 RegExp 對象。

下面的示例代碼用規則運算式來決定指定的字串是否是一個電子郵件地址。

## 

### \[JavaScript\]

```
str = "info@emurasoft.com";
re = new RegExp(
"^[\a-z0-9-]+(\\\.[\a-z0-9-]+)\*@[a-z0-9-]+(\\\.[a-z0-9-]+)\*(\\\.[a-z]{2,4})$", "i"
);
result = re.test( str );
if( result ) {
alert( "The email address is OK." );
}
else {
alert( "The email address is invalid." );
}
```

### \[VBScript\]

```
str = "info@emurasoft.com"
Set regEx = New RegExp
regEx.Pattern = "^[\a-z0-9-]+(\\.[\a-z0-9-]+)\*@[a-z0-9-]+(\\.[a-z0-9-]+)\*(\\.[a-z]{2,4})$"
regEx.IgnoreCase = True
result = regEx.Test( str )
If result Then
alert "The email address is OK."
Else
alert "The email address is invalid."
End If
```

## 參考

[Microsoft MSDN Library: Regular Expression Object (JavaScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

[Microsoft MSDN Library: RegExp Object (VBScript)](https://docs.microsoft.com/en-us/previous-versions//yab2dx62(v=vs.85))
