# Test メソッド (Regex オブジェクト)

正規表現が指定する文字列にマッチするかどうかをテストします。

## 

### \[JavaScript\]

```
b  = reg.Test( strText );
```

### \[VBScript\]

```
b  = reg.Test( strText )
```

### パラメータ

_strText_

テストする文字列を指定します。

## 戻り値

正規表現が指定する文字列にマッチすると True を返します。そうでなければ False を返します。

## 例

### \[JavaScript\]

```
re = editor.regex;
re.Engine = eeExFindRegexOnigmo;
re.Pattern = "^[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\\.[A-Z]{2,}$";
re.IgnoreCase = true;
b = re.Test( "john@test.com" );
if( b ) alert( "the regular expression matched" );
```

### \[VBScript\]

```
Set re = editor.regex
re.Engine = eeExFindRegexOnigmo
re.Pattern = "^[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$"
re.IgnoreCase = True
b = re.Test( "john@test.com" )
If b Then alert( "the regular expression matched" )
```

### バージョン

EmEditor Professional Version 15.9 以上で利用できます。
