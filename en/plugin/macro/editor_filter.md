# Editor\_Filter

Filters the document with the specified string and settings. You can use this inline function or explicitly send
the [EE\_FILTER](../message/ee_filter) message.

Editor\_Filter( HWND hwnd, LPCWSTR szFilter, int iColumn, UINT64 nFlags,
INT\_PTR xBegin, INT\_PTR xEnd );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_szFilter_

Specifies a string to search for.

_iColumn_

Specifies the index of the column of the text you want to search, or -1 if you want to search whole lines.

_nFlags_

You can specify a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_FIND\_BOOKMARKED\_ONLY | Matches bookmarked lines only. This flag cannot be combined with FLAG\_FIND\_UNBOOKMARKED\_ONLY. |
| FLAG\_FIND\_CASE | Matches cases. |
| FLAG\_FIND\_CONTINUE | Specifies the EE\_FILTER message called next time should not clear the filter. This filter is not applied immediately after this message is called. This flag is used when you want to create multiple levels of the filter. It is similar to the FLAG\_FIND\_KEEP\_PREVIOUS flag, but since the actual filter is not applied each time the message is called, this method works faster if there are multiple filter levels. |
| FLAG\_FIND\_CR\_LF | Matches lines of which the newline character is CR and LF. This flag must be combined with FLAG\_FIND\_MATCH\_NL. |
| FLAG\_FIND\_CR\_ONLY | Matches lines of which the newline character is CR only. This flag must be combined with FLAG\_FIND\_MATCH\_NL. |
| FLAG\_FIND\_ESCAPE | Uses escape sequences. |
| FLAG\_FIND\_FUZZY | Uses fuzzy matching. |
| FLAG\_FIND\_KEEP\_PREVIOUS | Specifies the EE\_FILTER message should not clear the existing filter before applying the new filter. This flag is used when you want to create multiple levels of the filter. |
| FLAG\_FIND\_LOGICAL\_OR | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
| FLAG\_FIND\_LF\_ONLY | Matches lines of which the newline character is LF only. This flag must be combined with FLAG\_FIND\_MATCH\_NL. |
| FLAG\_FIND\_LINK\_FILE | Specifies _pszFilter_ is the file path to a linked file that contains multiple search strings divided by newlines. If a tab character is included in a line, the search string is the first string not including the tab character. _pszFilter_ may be a relative path from the EmEditor install path. It may contain environment variables such as %USERPROFILE%. |
| FLAG\_FIND\_MATCH\_NL | Matches specified newline characters. This flag should be combined with FLAG\_FIND\_CR\_LF, FLAG\_FIND\_CR\_ONLY, FLAG\_FIND\_LF\_ONLY, and/or FLAG\_FIND\_NL\_OTHERS. |
| FLAG\_FIND\_NEGATIVE | Shows the Filter toolbar and excludes the lines that match the specified string. |
| FLAG\_FIND\_NL\_OTHERS | Matches lines without a newline character. These lines includes the last line of the file and very long lines that continue to the next line without a newline character. This flag must be combined with FLAG\_FIND\_MATCH\_NL. |
| FLAG\_FIND\_NUMBER\_RANGE | Matches a number range. This flag cannot be combined with FLAG\_FIND\_ESCAPE or FLAG\_FIND\_REG\_EXP. |
| FLAG\_FIND\_ONLY\_WORD | Searches only words. |
| FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
| FLAG\_FIND\_REMOVE\_LAST | Removes the last added filter level. |
| FLAG\_FIND\_UNBOOKMARKED\_ONLY | Matches unbookmarked lines only. This flag cannot be combined with FLAG\_FIND\_BOOKMARKED\_ONLY. |
| FLAG\_FIND\_WHOLE\_STRING | Matches whole strings. |

_xBegin_

Specifies the index of beginning of the column (in logical characters) of the text you want to search, or -1 if you want to
count the last portion of the text and specify as _xEnd_.

_xEnd_

Specifies the index of ending of the column (in logical characters) of the text you want to search, or -1 if you want to search
all the rest of the text.

## Return Values

The return value
is the number of the lines that match the specified string. If the specified string is an empty string, the return value is -1. If FLAG\_FIND\_CONTINUE is specified, the return value is 0.

## Version

Supported on EmEditor Professional Version 14.7 or later.
