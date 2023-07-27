# EE\_FIND\_IN\_FILESA

在指定路徑的多個檔案中搜尋一個 ANSI 字符串。被搜尋的檔案列表會顯示在當前視窗內。如果當前文檔被修改，EmEditor 會顯示是否將更改保存到當前檔案的提示消息框。您能明確地發送該消息或用
[Editor\_FindInFilesA](../macro/editor_findinfilesa) 內嵌函式。

EE\_FIND\_IN\_FILESA

wParam = 0;

lParam = (LPARAM) (GREP\_INFOA) pGrepInfo;

## 參數

_pGrepInfo_

指定一個指針指向 [GREP\_INFOA \
結構](../structure/grep_infoa)。

## Return Value

返回 FALSE，如果用戶中止，不然，返回 TRUE。

## 支持版本

支持 EmEditor 4.02 或之後的版本。
