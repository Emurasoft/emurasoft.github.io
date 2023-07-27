# EE\_GET\_ATTR

在指定位置检索配置与属性。你能明确地发送该消息或用 [Editor\_GetAttr](../macro/editor_getattr) 内联函数。

EE\_GET\_ATTR

wParam = 0;

lParam = (LPARAM) (ATTR\_INFO) pAI;

## 参数

_pAI_

指针指向 [ATTR\_INFO](../structure/attr_info) 结构。

## 返回值

返回值是 TRUE 如果成功，或 FALSE 如果不成功。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
