# EE\_QUERY\_STRING\_EX

查詢與指定的命令相關聯的字串。此消息支持超過 MAX\_PATH 字元的長檔案路徑。你能明確地發送該消息或用 [Editor\_QueryStringEx](../macro/editor_querystringex) 內嵌函式。

EE\_QUERY\_STRING

wParam = 0;

lParam = (LPARAM) (QUERY\_STRING\_INFO\*) pInfo;

## 參數

_pInfo_

> 指定一個指針指向 [**QUERY\_STRING\_INFO** 結構](../structure/query_string_info)。

## 返回值

> 如果成功，則返回值為 S\_OK。否則，返回值為負值。

## 支持版本

> 支持 EmEditor Professional Version 20.6 或之後的版本。
