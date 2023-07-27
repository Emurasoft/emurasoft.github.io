# Editor\_GetFilter

檢索目前的文檔的篩選字串及設定。你能用該內嵌函式或明確地發送
the [EE\_GET\_FILTER](../message/ee_filter) 消息。

Editor\_GetFilter( HWND hwnd, int iFilter, LPWSTR pszFilter, UINT cchFilter, int\* piColumn, UINT64\* pnFlags, INT\_PTR\* pxBegin, INT\_PTR\* pxEnd )

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pszFilter_

指定一個緩衝區來檢索篩選字串。

_cchFilter_

用字元數指定檢索篩選字串的緩衝區的大小。

_piColumn_

指定指針指向整數來檢索用篩選器過濾的文字的列索引。如果篩選文檔的所有列，即搜索「一整行」而非特定的列，那么這個索引值是 -1。

_pnFlags_

指定指針指向 64-bit 的整數來檢索標志。檢索的標志會是下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大小寫需符合。 |
| FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
| FLAG\_FIND\_LOGICAL\_OR | 指定一個邏輯或運算 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
| FLAG\_FIND\_NEGATIVE | 顯示篩選工具列并排除與指定字串符合的行。 |
| FLAG\_FIND\_ONLY\_WORD | 整個單字需符合。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |

_pxBegin_

指定指針指向整數來檢索要搜索的文字的起始欄的索引（用邏輯字元數）；這個值可以是 -1，如果文字的最后一部分被作為 _xEnd_。

_pxEnd_

指定指針指向整數來檢索要搜索的文字的末尾欄的索引（用邏輯字元數）；這個值可以是 -1，如果要搜索剩余的文字。

## 返回值

如果 iFilter 是 0 或更大的數字并且消息成功，返回值為 TRUE。如果 iFilter 是 -1，返回值是篩選器的數目。

## 版本

支持 EmEditor Professional Version 16.0 或之後的版本。
