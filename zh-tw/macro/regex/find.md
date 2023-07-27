# Find 方法 (Regex ��H)

用規則運算式搜尋指定的字串并返回一個 [Matches 集合](../matches/index) 如果發現符合。如果設定的是Global 屬性，這個方法能重複用同樣的參數來檢索幾個符合。

## 

### \[JavaScript\]

```
match  = reg.Find( strText );
```

### \[VBScript\]

```
match  = reg.Find( strText )
```

## 參數

_strText_

指定要用規則運算式搜尋的字串。

## 返回值

返回一個 [Matches 集合](../matches/index) 如果指定字串包含符合的規則運算式。該功能會返回 null 如果沒有找到符合。

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

支持 EmEditor Professional Version 15.9 或之後的版本。
