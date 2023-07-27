# Editor\_FindRegex

用規則運算式搜尋一個字串。您能直接用該內嵌函式或明確地發送 [EE\_FIND\_REGEX](../message/ee_find_regex) 消息。

Editor\_FindRegex( HWND hwnd, FIND\_REGEX\_INFO\* pFindRegexInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pFindRegexInfo_

指標至 [FIND\_REGEX\_INFO 結構](../structure/find_regex_info)。

## 返回值

如果一個符合指定規則運算式的字串被找到了，返回值是 TURE。如果指定的規則運算式沒有被找到，返回值是 FALSE。如果規則運算式存在語法錯誤或其他嚴重錯誤，返回值是 -1。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
