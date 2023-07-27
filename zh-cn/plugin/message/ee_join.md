# EE\_JOIN

按指定键列,用一个与 JOIN 操作类似的方法合并两个 CSV 文档,并创建一个新文档。你可以明确地发送该消息或用 [Editor\_Join](../macro/editor_join) 内联函数｡

EE\_JOIN

wParam = (WPARAM) (JOIN\_INFO\*) pJoinInfo;

lParam = 0;

## 参数

_pJoinInfo_

指针指向 [JOIN\_INFO](../structure/join_info) 结构｡

## 返回值

返回值是新文档的行数｡返回值为负数如果发生错误的话｡如果发生错误,返回值是下列值之一:

|     |     |
| --- | --- |
| E\_DOCUMENT\_1\_NOT\_FOUND | 无法找到第一个文档｡ |
| E\_DOCUMENT\_2\_NOT\_FOUND | 无法找到第二个文档｡ |
| E\_COLUMN\_1\_NOT\_FOUND | 无法找到第一列｡ |
| E\_COLUMN\_2\_NOT\_FOUND | 无法找到第二列｡ |
| E\_SELECT\_SYNTAX | 选择的字符串中有语法错误｡ |
| E\_SELECT\_DOCUMENT\_NOT\_FOUND | 无法在选择的字符串中找到指定的文档｡ |
| E\_SELECT\_COLUMN\_NOT\_FOUND | 无法在选择的字符串中找到指定列｡ |
| E\_DIFFERENT\_CSV\_MODE | 不同的 CSV 模式。 |
| E\_NOT\_MDI | 必须启用 Tab。 |
| E\_WRITE\_TEMP\_FILE | 临时文件写入错误。 |
| E\_ABORT | 被用户中止。 |
| E\_FAIL | 未指定的错误。 |

## 版本

支持 EmEditor 14.8 或之后的版本。
