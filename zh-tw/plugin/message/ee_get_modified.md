# EE\_GET\_MODIFIED

檢索文本的修改狀態。您能明確地發送該消息或用 [Editor\_GetModified](../macro/editor_getmodified) 或 [Editor\_DocGetModified](../macro/editor_docgetmodified) 內嵌函式。

EE\_GET\_MODIFIED

wParam = (WPARAM) MAKEWPARAM(0, iDoc+1);

lParam = hDoc;

## 參數

_iDoc_

> 指定目標文件的索引。指定目標文件的索引。應當指定一個從 1 開始的索引在 wParam 的高字處。如果 wParam 的高字處指定了 0，那么目前使用中的文件就會成為目標文件。

_hDoc_

> （可選）指定目標文件的控點。如果指定此參數，iDoc 必須為 0。

## 返回值

> 如果文本被修改，返回值是 TRUE。如果文本沒有被修改，返回值是 FALSE。
