# Find 方法 (Regex ����)

用正则表达式搜索指定的字符串并返回一个 [Matches 集合](../matches/index) 如果发现匹配。如果设定的是Global 属性，这个方法能重复用同样的参数来检索几个匹配。

## 

### \[JavaScript\]

```
match  = reg.Find( strText );
```

### \[VBScript\]

```
match  = reg.Find( strText )
```

## 参数

_strText_

指定要用正则表达式搜索的字符串。

## 返回值

返回一个 [Matches 集合](../matches/index) 如果指定字符串包含匹配的正则表达式。该功能会返回 null 如果没有找到匹配。

## 示例

### \[JavaScript\]

```
re = editor.regex;
re.Engine = eeExFindRegexOnigmo;
re.Pattern = "[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\\.[A-Z]{2,}";
re.IgnoreCase = true;
re.OnlyWord = false;
matches = re.Find( "The email address is john@test.com." );
if( matches ) {
match = matches.Item(0);
alert( "Found: FirstIndex = " + match.FirstIndex + " , Length = " + match.Length + ", Value = " + match.Value );
}
```

### \[VBScript\]

```
Set re = editor.regex
re.Engine = eeExFindRegexOnigmo
re.Pattern = "[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}"
re.IgnoreCase = True
re.OnlyWord = False
Set matches = re.Find( "The email address is john@test.com." )
If Not IsNull( matches ) Then
Set match = matches.Item(0)
alert( "Found: FirstIndex = " & match.FirstIndex & " , Length = " & match.Length & ", Value = " & match.Value )
End If
```

## 版本

支持 EmEditor Professional Version 15.9 或之后的版本。
