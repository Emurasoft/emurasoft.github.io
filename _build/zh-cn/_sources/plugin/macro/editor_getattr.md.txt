# Editor\_GetAttr

在剪贴板记录中的指定位置处删除文本。你能直接用该内联函数或明确地发送 [EE\_GET\_ATTR](../message/ee_get_attr)
消息。

Editor\_GetAttr( HWND hwnd, ATTR\_INFO\* pAI );

## 参数

_pAI_

> 指针指向 [ATTR\_INFO](../structure/attr_info) 结构。

## 返回值

> 返回值是 TRUE 如果成功，或 FALSE 如果不成功。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。