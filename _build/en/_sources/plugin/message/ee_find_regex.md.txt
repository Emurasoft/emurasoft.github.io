# EE\_FIND\_REGEX

用規則運算式搜尋一個字符串。您能明確地發送該消息或用 [Editor\_FindRegex](../macro/editor_findregex) 內嵌函式。

EE\_FIND\_REGEX

wParam = 0;

lParam = (LPARAM) (FIND\_REGEX\_INFO\*) pFindRegexInfo;

## 參數

_pFindRegexInfo_

> Pointer to the [FIND\_REGEX\_INFO structure](../structure/find_regex_info).

## 返回值

> 如果一個匹配指定規則運算式的字符串被找到了，返回值是 TURE。如果指定的規則運算式沒有被找到，返回值是 FALSE。如果規則運算式存在語法錯誤或其他嚴重錯誤，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。