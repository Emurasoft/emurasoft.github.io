# Editor\_FindRegex

用正则表达式搜索一个字符串。你能直接用该内联函数或明确地发送 [EE\_FIND\_REGEX](../message/ee_find_regex) 消息。

Editor\_FindRegex( HWND hwnd, FIND\_REGEX\_INFO\* pFindRegexInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pFindRegexInfo_

> 指针指向 [FIND\_REGEX\_INFO 结构](../structure/find_regex_info)。

## 返回值

> 如果一个匹配指定正则表达式的字符串被找到了，返回值是 TURE。如果指定的正则表达式没有被找到，返回值是 FALSE。如果正则表达式存在语法错误或其他严重错误，返回值是 -1。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
