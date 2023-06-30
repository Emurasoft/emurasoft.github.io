# Test 方法 (Regex ����)

测试正则表达式是否与指定字符串成功匹配。

#### \[JavaScript\]

_b_  = reg. **Test**( _strText_ );

#### \[VBScript\]

_b_  = reg. **Test**( _strText_ )

## 参数

_strText_

指定一个要测试的字符串。

## 返回值

返回 True 如果正则表达式成功与指定字符串匹配，否则返回 False。

## 示例

#### \[JavaScript\]

re = editor.regex;

re.Engine = eeExFindRegexOnigmo;

re.Pattern = "^\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\\.\[A-Z\]{2,}$";

re.IgnoreCase = true;

b = re.Test( "john@test.com" );

if( b ) alert( "正则表达式匹配" );

#### \[VBScript\]

Set re = editor.regex

re.Engine = eeExFindRegexOnigmo

re.Pattern = "^\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\.\[A-Z\]{2,}$"

re.IgnoreCase = True

b = re.Test( "john@test.com" )

If b Then alert( "正则表达式匹配" )

## 版本

支持 EmEditor Professional Version 15.9 或之后的版本。