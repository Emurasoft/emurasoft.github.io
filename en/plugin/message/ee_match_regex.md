# EE\_MATCH\_REGEX

Determines whether a string matches a specified regular expression. You can send this message
explicitly or use the [Editor\_MatchRegex](../macro/editor_matchregex) inline function.

```
EE_MATCH_REGEX
wParam = 0;
lParam = (LPARAM) (MATCH_REGEX_INFO_EX*) pMatchRegexInfo;
```

## Parameters

_pMatchRegexInfo_

Pointer to the [MATCH\_REGEX\_INFO\_EX structure](../structure/match_regex_info_ex) or [MATCH\_REGEX\_INFO structure](../structure/match_regex_info).

## Return Values

If a string matches the specified regular expression, the return value is TRUE. If a string does not match the specified regular expression, the return
value is FALSE. If the regular expression has a syntax error or another fatal error occurs,
the return value is -1.

## Version

Supported on Version 6.00 or later.
