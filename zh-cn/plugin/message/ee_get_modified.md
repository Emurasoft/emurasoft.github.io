# EE\_GET\_MODIFIED

检索文本的修改状态。你能明确地发送该消息或用 [Editor\_GetModified](../macro/editor_getmodified) 或 [Editor\_DocGetModified](../macro/editor_docgetmodified) 内联函数。

EE\_GET\_MODIFIED

wParam = (WPARAM) MAKEWPARAM(0, iDoc+1);

lParam = hDoc;

## 参数

_iDoc_

指定目标文档的索引。应当在 wParam 的高字处指定一个以 1 为基准的索引。如果 wParam 的高字处指定了 0，那么当前活动的文档就会成为目标文档。

_hDoc_

（可选）指定目标文档的句柄。如果指定此参数，iDoc 必须为 0。

## 返回值

如果文本被修改，返回值是 TRUE。如果文本没有被修改，返回值是 FALSE。
