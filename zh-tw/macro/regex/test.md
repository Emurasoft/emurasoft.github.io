# Test 方法 (Regex ��H)

測試規則運算式是否與指定字串成功符合。

## 

### \[JavaScript\]

```
b  = reg.Test( strText );
```

### \[VBScript\]

```
b  = reg.Test( strText )
```

## 參數

_strText_

指定一個要測試的字串。

## 返回值

返回 True 如果規則運算式成功與指定字串符合，否則返回 False。

## 示例

### \[JavaScript\]

```
re = editor.regex;
re.Engine = eeExFindRegexOnigmo;
re.Pattern = "^[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\\.[A-Z]{2,}$";
re.IgnoreCase = true;
b = re.Test( "john@test.com" );
if( b ) alert( "規則運算式符合" );
```

### \[VBScript\]

```
Set re = editor.regex
re.Engine = eeExFindRegexOnigmo
re.Pattern = "^[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$"
re.IgnoreCase = True
b = re.Test( "john@test.com" )
If b Then alert( "規則運算式符合" )
```

## 版本

支持 EmEditor Professional Version 15.9 或之後的版本。
