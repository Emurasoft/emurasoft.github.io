# Replace 方法 (Regex 對象)

用規則運算式搜尋指定的字串，并用指定的字串取代。如果設定的是 **Global** 屬性，這個方法會取代字串中所有可能的符合。

## 

### \[JavaScript\]

```
strResult = reg.Replace( strText, strReplace );
```

### \[VBScript\]

```
strResult = reg.Replace( strText, strReplace )
```

## 參數

_strText_

指定要用規則運算式搜尋的字串。

_strReplace_

指定要取代為的字串。

## 返回值

返回新的字串。

## 示例

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

## 版本

支持 EmEditor Professional Version 15.9 或之後的版本。
