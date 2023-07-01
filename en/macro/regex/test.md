# Test Method (Regex Object)

Tests the regular expression is successfully matched against the specified string.

#### \[JavaScript\]

_b_  = reg. **Test**( _strText_ );

#### \[VBScript\]

_b_  = reg. **Test**( _strText_ )

## Parameters

_strText_

Specifies a string to test.

## Return Values

Returns True if the regular expression is successfully matched against the specified string, or False if not.

## Examples

#### \[JavaScript\]

re = editor.regex;

re.Engine = eeExFindRegexOnigmo;

re.Pattern = "^\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\\.\[A-Z\]{2,}$";

re.IgnoreCase = true;

b = re.Test( "john@test.com" );

if( b ) alert( "the regular expression matched" );

#### \[VBScript\]

Set re = editor.regex

re.Engine = eeExFindRegexOnigmo

re.Pattern = "^\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\.\[A-Z\]{2,}$"

re.IgnoreCase = True

b = re.Test( "john@test.com" )

If b Then alert( "the regular expression matched" )

## Version

Supported in EmEditor Professional Version 15.9 or later.
