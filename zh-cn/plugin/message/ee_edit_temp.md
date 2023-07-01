# EE\_EDIT\_TEMP

把临时文本作为一个新文档打开，或激活、保存或关闭已存在的临时文本。你能明确地发送该消息或用 [Editor\_ActivateTemp](../macro/editor_activatetemp)， [Editor\_CloseTemp](../macro/editor_closetemp)，
[Editor\_EditTemp](../macro/editor_edittemp)，或 [Editor\_SaveTemp](../macro/editor_savetemp) 内联函数。

EE\_EDIT\_TEMP

wParam = 0;

lParam = (LPARAM) (TEMP\_INFO) pTI;

## 参数

_pTI_

> 指针指向 [TEMP\_INFO](../structure/temp_info) 结构。

## 返回值

> 返回值是新文档的 ID。然而，当关闭一个临时文本时，不使用返回值。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
