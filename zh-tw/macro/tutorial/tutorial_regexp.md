# 使用規則運算式 (�е{)

要使用規則運算式，請用 RegExp 對象。

下面的示例代碼用規則運算式來決定指定的字串是否是一個電子郵件地址。

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

## 參考

)