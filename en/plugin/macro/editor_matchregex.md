# Editor\_MatchRegex

Determines whether a string matches a specified regular expression. You can use this inline function or explicitly send the [EE\_MATCH\_REGEX](../message/ee_match_regex) message.

Editor\_MatchRegex( HWND hwnd, MATCH\_REGEX\_INFO\_EX\* pMatchRegexInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pMatchRegexInfo_

> Pointer to the [MATCH\_REGEX\_INFO\_EX structure](../structure/match_regex_info_ex) or [MATCH\_REGEX\_INFO structure](../structure/match_regex_info).

## Return Values

> If a string matches the specified regular expression, the return value is TRUE. If a string does not match the specified regular expression, the return value is FALSE. If the regular expression has a syntax error or another fatal error occurs,
> the return value is -1.

## Version

> Supported on Version 6.00 or later.