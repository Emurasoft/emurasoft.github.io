# 獲取電腦使用者的名稱 (教程)

要獲取電腦使用者的名稱，用 WshNetwork 對象的 UserName 屬性。

下面的示例演示了如何獲取目前的電腦使用者的名稱:

## 

### \[JavaScript (JScript)\]

```
WshNetwork = new ActiveXObject( "WScript.Network" );
alert( "User Name = " + WshNetwork.UserName );
```

### \[VBScript\]

```
Set WshNetwork = CreateObject( "WScript.Network" )
alert "User Name = " & WshNetwork.UserName
```

## 參考

[Microsoft MSDN Library: UserName Property](https://docs.microsoft.com/en-us/previous-versions/3fxhka75(v=vs.71))
