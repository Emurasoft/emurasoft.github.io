# EE\_CONVERT\_EX

转换字符。你能明确地发送该消息或用 [Editor\_Convert](../macro/editor_convert) 内联函数。

EE\_CONVERT

wParam = (WPARAM) (CONVERT\_INFO\*)pInfo;

lParam = 0;

## 参数

_pInfo_

> 指定指针指向 [CONVERT\_INFO](../structure/convert_info) 结构。

## 返回值

> 如果消息成功，返回值为非零。如果消息失败，返回值为零。

## 版本

> 支持 EmEditor Professional v22.1 或之后的版本。