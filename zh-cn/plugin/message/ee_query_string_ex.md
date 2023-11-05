# EE\_QUERY\_STRING\_EX

查询与指定的命令相关联的字符串。此消息支持超过 MAX\_PATH 字符的长文件路径。你能明确地发送该消息或用 [Editor\_QueryStringEx](../macro/editor_querystringex) 内联函数。

EE\_QUERY\_STRING\_EX

wParam = 0;

lParam = (LPARAM) (QUERY\_STRING\_INFO\*) pInfo;

## 参数

_pInfo_

指定一个指针指向 [**QUERY\_STRING\_INFO** 结构](../structure/query_string_info)。

## 返回值

如果成功，则返回值为 S\_OK。否则，返回值为负值。

## 支持版本

支持 EmEditor Professional Version 20.6 或之后的版本。
