# 정규식 표현 사용 (Ʃ�丮��)

정규식 표현을 사용하려면 RegExp 개체를 사용합니다.

다음의 예제 코드는 지정된 문자열이 이메일 주소인지 아닌지의 여부를 구분하는 정규식 표현을 사용합니다.

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

## 참조:
