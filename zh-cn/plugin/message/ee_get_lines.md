# EE\_GET\_LINES

检索在 EmEditor 中的行数。你能明确地发送该消息或用 [Editor\_DocGetLines](../macro/editor_docgetlines) 内联函数或 [Editor\_GetLines](../macro/editor_getlines) 内联函数。

EE\_QUERY\_STATUS

wParam = (WPARAM) MAKEWPARAM(nLogical, iDoc+1);

lParam = hDoc;

## 参数

_nLogical_

> 指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | POS\_VIEW | 显示坐标 |
> | POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
> | POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |

_iDoc_

> 指定目标文档的索引。应当指定一个以 1 为基准的索引在 wParam 参数的高字处。如果 wParam 参数的高字处指定了 0，那么当前活动的文档就会成为目标文档。

_hDoc_

> （可选）指定目标文档的句柄。如果指定此参数，iDoc 必须为 0。

## 返回值

> 返回在 EmEditor 中的行数。如果最后的一行以回车结尾，那么最后的一行也会被算在内。如果文本为空，返回 1。