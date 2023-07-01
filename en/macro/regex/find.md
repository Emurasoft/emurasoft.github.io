# Find Method (Regex Object)

Searches the specified string for the regular expression and returns a [**Matches** collection](../matches/index) if a match is found. If the **Global** property is set, this method can be repeated with the same parameter to retrieve several matches.

#### \[JavaScript\]

match  = reg. **Find**( _strText_ );

#### \[VBScript\]

match  = reg. **Find**( _strText_ )

## Parameters

_strText_

Specifies a string to search for the regular expression.

## Return Values

Returns a [Matches collection](../matches/index) if the specified string contains the matched regular expression. This functions returns null if no match is found.

## Examples

#### \[JavaScript\]

re = editor.regex;

re.Engine = eeExFindRegexOnigmo;

re.Pattern = "\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\\.\[A-Z\]{2,}";

re.IgnoreCase = true;

re.OnlyWord = false;

matches = re.Find( "The email address is john@test.com." );

if( matches ) {

match = matches.Item(0);

alert( "Found: FirstIndex = " + match.FirstIndex + " , Length = " + match.Length + ", Value = " + match.Value );

}

#### \[VBScript\]

Set re = editor.regex

re.Engine = eeExFindRegexOnigmo

re.Pattern = "\[A-Z0-9.\_%+-\]+@\[A-Z0-9.-\]+\\.\[A-Z\]{2,}"

re.IgnoreCase = True

re.OnlyWord = False

Set matches = re.Find( "The email address is john@test.com." )

If Not IsNull( matches ) Then

Set match = matches.Item(0)

alert( "Found: FirstIndex = " & match.FirstIndex & " , Length = " & match.Length & ", Value = " & match.Value )

End If

## Version

Supported in EmEditor Professional Version 15.9 or later.
