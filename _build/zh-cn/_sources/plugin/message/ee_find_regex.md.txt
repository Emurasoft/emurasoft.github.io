# EE\_FIND\_REGEX

用正则表达式搜索一个字符串。你能明确地发送该消息或用 [Editor\_FindRegex](../macro/editor_findregex) 内联函数。

EE\_FIND\_REGEX

wParam = 0;

lParam = (LPARAM) (FIND\_REGEX\_INFO\*) pFindRegexInfo;

## 参数

_pFindRegexInfo_

> Pointer to the [FIND\_REGEX\_INFO structure](../structure/find_regex_info).

## 返回值

> 如果一个匹配指定正则表达式的字符串被找到了，返回值是 TURE。如果指定的正则表达式没有被找到，返回值是 FALSE。如果正则表达式存在语法错误或其他严重错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。