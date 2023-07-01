# EE\_COMPARE

比较两个文件。你能明确地发送该消息或用 [Editor\_Compare](../macro/editor_compare) 内联函数。

EE\_COMPARE

wParam = (WPARAM) (COMPARE\_INFO\*) pCompareInfo;

lParam = 0;

## 参数

_pCompareInfo_

> 指针指向 [COMPARE\_INFO](../structure/compare_info) 结构。

## 返回值

> 返回值可以是以下值之一。 如果发生错误，返回值为负值。
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 找不到第一个文件。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 找不到第二个文件。 |
> | E\_FAIL | 未指定的错误。 |
> | E\_NOT\_MDI | 必须启用 Tab。 |
> | S\_DIFF | 两个文档不相同。 |
> | S\_MATCHED | 两个文档相同。 |
> | S\_MATCHED\_IGNORED | 除了被忽略的地方外，两个文档是相同的。 |

## 支持版本

> 支持 EmEditor Professional v17.7 或之后的版本。
