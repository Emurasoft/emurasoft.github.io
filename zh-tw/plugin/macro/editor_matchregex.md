# Editor\_MatchRegex

決定一個字串是否與一個指定的規則運算式相符合。您能直接用該內嵌函式或明確地發送 [EE\_MATCH\_REGEX](../message/ee_match_regex) 消息。

Editor\_MatchRegex( HWND hwnd, MATCH\_REGEX\_INFO\* pMatchRegexInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pMatchRegexInfo_

> 指標至 [MATCH\_REGEX\_INFO 結構](../structure/match_regex_info)。

## 返回值

> 如果一個字串與指定的規則運算式相符合，返回值是 TRUE。如果一個字串與指定的規則運算式不符合，返回值是 FALSE。如果規則運算式有語法錯誤或存在另一個嚴重錯誤，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。
