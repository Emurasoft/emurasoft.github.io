# Editor\_ActivateTemp

把临时文本作为一个新文档打开。你能直接用该内联函数或明确地发送 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息。

Editor\_ActivateTemp( HWND hwnd, UINT nEditID, POINT\_PTR\* pptInitialCaret = NULL );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nEditID_

> 指定你想要激活的临时文本的 ID。S

_pptInitialCaret_

> 指定初始光标位置。

## 返回值

> 返回值是新文档的 ID。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。
