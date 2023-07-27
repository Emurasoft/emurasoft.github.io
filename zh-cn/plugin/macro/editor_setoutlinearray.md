# Editor\_SetOutlineArray

为指定的多行设置大纲级别。你能直接用该内联函数或明确地发送
[EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 消息。

Editor\_SetOutlineArray( HWND hwnd, INT\_PTR nStartLine, INT\_PTR nCount, BYTE\* pLevelData );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nStartLine_

指定多行的首行。

_nCount_

指定多行的行数。

_pLevelData_

指定决定大纲级别的字节数组。

## 返回值

返回值是 FALSE 如果没有变更。否则，返回值是 TRUE。

## 支持版本

支持 EmEditor 13 或之后的版本。
