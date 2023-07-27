# コンピュータのユーザー名を取得する ()

コンピュータのユーザー名を取得するには、WshNetwork オブジェクトの UserName プロパティを利用することができます。

この例では、現在のコンピュータのユーザー名を取得して表示します。

## 

### \[JavaScript (JScript)\]

WshNetwork = new ActiveXObject( "WScript.Network" );

alert( "User Name = " + WshNetwork.UserName );

### \[VBScript\]

```
Set WshNetwork = CreateObject( "WScript.Network" )
alert "User Name = " & WshNetwork.UserName
```

## 参考

)
