# 获取电脑用户的名称 (�̳�)

要获取电脑用户的名称，用 WshNetwork 对象的 UserName 属性。

下面的示例演示了如何获取当前电脑用户的名称:

#### \[JavaScript (JScript)\]

WshNetwork = new ActiveXObject( "WScript.Network" );

alert( "User Name = " + WshNetwork.UserName );

#### \[VBScript\]

Set WshNetwork = CreateObject( "WScript.Network" )

alert "User Name = " & WshNetwork.UserName

## 参考

)
