# Using Regular Expressions (Tutorial)

To use regular expressions, use the RegExp Object.

The following example code uses regular expressions to determine whether or not the specified string is an email address.

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

## References



)
