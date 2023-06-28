# EE\_GET\_ACTIVE\_STRING

检索活动字符串。你能明确地发送该消息或用 [Editor\_GetActiveString](../macro/editor_getactivestring) 内联函数。

EE\_GET\_ACTIVE\_STRING

wParam = (WPARAM) 0;

lParam = (LPARAM) (ACTIVE\_STRING\_INFO\*) pInfo;

## 参数

_pInfo_

> 指针指向 [ACTIVE\_STRING\_INFO](../structure/active_string_info) 结构。

## 返回值

> 返回要检索包含终止 NULL 字符的活动字符串所需的缓冲区字符数。

## 版本

> 支持 EmEditor Professional Version 16.9 或之后的版本。