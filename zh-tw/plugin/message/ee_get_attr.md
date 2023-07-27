# EE\_GET\_ATTR

在指定位置檢索配置與屬性。您能明確地發送該消息或用 [Editor\_GetAttr](../macro/editor_getattr) 內嵌函式。

EE\_GET\_ATTR

wParam = 0;

lParam = (LPARAM) (ATTR\_INFO) pAI;

## 參數

_pAI_

指針指向 [ATTR\_INFO](../structure/attr_info) 結構。

## 返回值

返回值是 TRUE 如果成功，或 FALSE 如果不成功。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
