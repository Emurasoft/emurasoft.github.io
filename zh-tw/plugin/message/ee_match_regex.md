# EE\_MATCH\_REGEX

決定一個字符串是否與一個指定的規則運算式相匹配。您能明確地發送該消息或用 [Editor\_MatchRegex](../macro/editor_matchregex) 內嵌函式。

```
EE_MATCH_REGEX
wParam = 0;
lParam = (LPARAM) (MATCH_REGEX_INFO*) pMatchRegexInfo;
```

## 參數

_pMatchRegexInfo_

指針指向 [MATCH\_REGEX\_INFO 結構](../structure/match_regex_info)。

## 返回值

如果一個字符串與指定的規則運算式相匹配，返回值是 TRUE。如果一個字符串與指定的規則運算式不匹配，返回值是 FALSE。如果規則運算式有語法錯誤或存在另一個嚴重錯誤，返回值是 -1。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
