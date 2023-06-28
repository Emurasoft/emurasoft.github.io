# EE\_MATCH\_REGEX

决定一个字符串是否与一个指定的正则表达式相匹配。你能明确地发送该消息或用 [Editor\_MatchRegex](../macro/editor_matchregex) 内联函数。

EE\_MATCH\_REGEX

wParam = 0;

lParam = (LPARAM) (MATCH\_REGEX\_INFO\*) pMatchRegexInfo;

## 参数

_pMatchRegexInfo_

> 指针指向 [MATCH\_REGEX\_INFO 结构](../structure/match_regex_info)。

## 返回值

> 如果一个字符串与指定的正则表达式相匹配，返回值是 TRUE。如果一个字符串与指定的正则表达式不匹配，返回值是 FALSE。如果正则表达式有语法错误或存在另一个严重错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。