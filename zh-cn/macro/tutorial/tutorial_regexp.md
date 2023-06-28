# 使用正则表达式

要使用正则表达式，请用 RegExp 对象。

下面的示例代码用正则表达式来决定指定的字符串是否是一个电子邮件地址。

#### \[JavaScript\]

str = "info@emurasoft.com";

re = new RegExp(
"^\[\_a-z0-9-\]+(\\\.\[\_a-z0-9-\]+)\*@\[a-z0-9-\]+(\\\.\[a-z0-9-\]+)\*(\\\.\[a-z\]{2,4})$", "i"
);

result = re.test( str );

if( result ) {

alert( "The email address is OK." );

}

else {

alert( "The email address is invalid." );

}

#### \[VBScript\]

str = "info@emurasoft.com"

Set regEx = New RegExp

regEx.Pattern =
"^\[\_a-z0-9-\]+(\\.\[\_a-z0-9-\]+)\*@\[a-z0-9-\]+(\\.\[a-z0-9-\]+)\*(\\.\[a-z\]{2,4})$"

regEx.IgnoreCase = True

result = regEx.Test( str )

If result Then

alert "The email address is OK."

Else

alert "The email address is invalid."

End If

## 参考

)