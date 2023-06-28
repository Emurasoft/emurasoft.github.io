# FILTER\_INFO

用於 [EE\_FILTER](../message/ee_filter) 消息。

typedef struct \_FILTER\_INFO {

UINT     cchSize;

UINT     flags;

int      iColumn;

LPCWSTR  pszFilter;

INT\_PTR  xBegin;

INT\_PTR  xEnd;

} FILTER\_INFO;

## 欄位

_cch_

> 指定這個結構的大小，sizeof( FILTER\_INFO )。

_flags_

> 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 大小寫需符合。 |
> | FLAG\_FIND\_CONTINUE | 指定下次調用的 EE\_FILTER 消息不會清除篩選記錄。在調用這個消息之後，這個篩選不會被馬上應用。您可以在您要進行多個級別的篩選時，使用這個標志。它與 FLAG\_FIND\_KEEP\_PREVIOUS 標志相同，但由于實際的篩選不會在每次調用消息時被應用，這個方法更適用於多個篩選級別。 |
> | FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
> | FLAG\_FIND\_KEEP\_PREVIOUS | 指定 EE\_FILTER 消息不會在應用新篩選前清除已存在的篩選記錄。您可以在您要進行多個級別的篩選時，使用這個標志。 |
> | FLAG\_FIND\_LOGICAL\_OR | 指定一個運算邏輯分離 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
> | FLAG\_FIND\_NEGATIVE | 顯示篩選工具列并排除與指定字串符合的行。 |
> | FLAG\_FIND\_ONLY\_WORD | 整個單字需符合。 |
> | FLAG\_FIND\_REG\_EXP | 使用一個規則運算式。 |
> | eeFindRemoveLast | 刪除前一次添加的篩選級別。 |

_iColumn_

> 指定您想要搜尋的文字的欄位的索引，或指定 -1 如果您想要搜尋整行。如果您要用字元數把開始以及結束的文字指定為 _xBegin_ 和 _xEnd_，可以指定 -2。

_pszFilter_

> 指定一個要搜尋的字串。

_xBegin_

> 指定您想要搜尋的文字的欄位開始的索引 (用邏輯字元數) ；您也可以指定 -1 如果您想要把文字的最后一部分作為 _xEnd_。要使這個欄位有效， _iColumn_ 值必須是 -2。

_xEnd_

> 指定您想要搜尋的文字的欄位結束的索引 (用邏輯字元數) ；您也可以指定 -1 如果您想要搜尋所有剩下的文字。要使這個欄位有效， _iColumn_ 值必須是 -2。

## 版本

> 支持 EmEditor Professional 14.7 或之後的版本。