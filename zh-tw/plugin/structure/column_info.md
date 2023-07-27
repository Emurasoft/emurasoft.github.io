# COLUMN\_INFO

用於 [SORT\_INFO 結構](sort_info)。

typedef struct \_COLUMN\_INFO {

int iCol;

UINT nFlags;

} COLUMN\_INFO;

## 欄位

_iCol_

指定要排序的列。

_nFlags_

指定下列值的組合。

|     |     |
| --- | --- |
| SORT\_ASCEND | 按升序排序。 |
| SORT\_DESCEND | 按降序排序。 |
| SORT\_DATE | 排序日期和時間。 |
| SORT\_LENGTH | 按文字長度排序。 |
| SORT\_NUM | 排序數字。 |
| SORT\_TEXT | 按字母順序排序文字。 |
| SORT\_WORDS | 按字數排序文字。 |

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。
