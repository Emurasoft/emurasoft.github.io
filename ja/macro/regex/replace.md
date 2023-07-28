# Replace メソッド (Regex オブジェクト)

指定する文字列から正規表現を検索し、指定する文字列で置換します。Global プロパティが設定されている場合、このメソッドは文字列中のすべての可能なマッチを置換します。

## 

### \[JavaScript\]

```
strResult = reg.Replace( strText, strReplace );
```

### \[VBScript\]

```
strResult = reg.Replace( strText, strReplace )
```

### パラメータ

_strText_

正規表現が検索される文字列を指定します。

_strReplace_

置換する文字列を指定します。

## 戻り値

新しい文字列を返します。

## 例

### \[JavaScript\]

```
re = editor.regex;
re.Engine = eeExFindRegexOnigmo;
re.Pattern = "([A-Z0-9.\%+-]+)@([A-Z0-9.-]+\\\.[A-Z]{2,})";
re.IgnoreCase = true;
re.OnlyWord = false;
strOrg = "The email address is john@test.com."
strNew = re.Replace( strOrg, "\\\1 at \\\2" );
if( strOrg != strNew ) {
alert( strNew );
}
```

### \[VBScript\]

```
Set re = editor.regex
re.Engine = eeExFindRegexOnigmo
re.Pattern = "([A-Z0-9.\%+-]+)@([A-Z0-9.-]+\\.[A-Z]{2,})"
re.IgnoreCase = True
re.OnlyWord = False
strOrg = "The email address is john@test.com."
strNew = re.Replace( strOrg, "\\1 at \\2" )
If strOrg <> strNew Then
alert( strNew )
End If
```

### バージョン

EmEditor Professional Version 15.9 以上で利用できます。
