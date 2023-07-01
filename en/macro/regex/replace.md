# Replace Method (Regex Object)

Searches the specified string for the regular expression and replace with the specified string. If the **Global** property is set, this method replaces all possible matches in the string.

#### \[JavaScript\]

_strResult_ = reg. **Replace**( _strText_, _strReplace_ );

#### \[VBScript\]

_strResult_ = reg. **Replace**( _strText_, _strReplace_ )

## Parameters

_strText_

Specifies a string to search for the regular expression.

_strReplace_

Specifies a string to replace with.

## Return Values

Returns the new string.

## Examples

#### \[JavaScript\]

re = editor.regex;

re.Engine = eeExFindRegexOnigmo;

re.Pattern = "(\[A-Z0-9.\_%+-\]+)@(\[A-Z0-9.-\]+\\\.\[A-Z\]{2,})";

re.IgnoreCase = true;

re.OnlyWord = false;

strOrg = "The email address is john@test.com."

strNew = re.Replace( strOrg, "\\\1 at \\\2" );

if( strOrg != strNew ) {

alert( strNew );

}

#### \[VBScript\]

Set re = editor.regex

re.Engine = eeExFindRegexOnigmo

re.Pattern = "(\[A-Z0-9.\_%+-\]+)@(\[A-Z0-9.-\]+\\.\[A-Z\]{2,})"

re.IgnoreCase = True

re.OnlyWord = False

strOrg = "The email address is john@test.com."

strNew = re.Replace( strOrg, "\\1 at \\2" )

If strOrg <> strNew Then

alert( strNew )

End If

## Version

Supported in EmEditor Professional Version 15.9 or later.
