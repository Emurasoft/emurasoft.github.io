# EE\_GET\_LINES

檢索在 EmEditor 中的行數。您能明確地發送該消息或用 [Editor\_DocGetLines](../macro/editor_docgetlines) 內嵌函式或 [Editor\_GetLines](../macro/editor_getlines) 內嵌函式。

EE\_QUERY\_STATUS

wParam = (WPARAM) MAKEWPARAM(nLogical, iDoc+1);

lParam = hDoc;

## 參數

_nLogical_

指定下列值之一。

| 值 | 含義 |
| --- | --- |
| POS\_VIEW | 顯示坐標 |
| POS\_LOGICAL\_A | 邏輯坐標 (把雙位元字符計為兩個) |
| POS\_LOGICAL\_W | 邏輯坐標 (把雙位元字符計為一個) |

_iDoc_

指定目標文件的索引。應當指定一個從 1 開始的索引在 wParam 參數的高字處。如果 wParam 參數的高字處指定了 0，那么目前使用中的文件就會成為目標文件。

_hDoc_

（可選）指定目標文件的控點。如果指定此參數，iDoc 必須為 0。

## 返回值

返回在 EmEditor 中的行數。如果最后的一行以回車結尾，那么最后的一行也會被算在內。如果文本為空，返回 1。
