# Replace 方法 (Regex 对象)

用正则表达式搜索指定的字符串，并用指定的字符串替换。如果设定的是 **Global** 属性，这个方法会替换字符串中所有可能的匹配。

## 

### \[JavaScript\]

```
strResult = reg.Replace( strText, strReplace );
```

### \[VBScript\]

```
strResult = reg.Replace( strText, strReplace )
```

## 参数

_strText_

指定要用正则表达式搜索的字符串。

_strReplace_

指定要替换为的字符串。

## 返回值

返回新的字符串。

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

支持 EmEditor Professional Version 15.9 或之后的版本。
