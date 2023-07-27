# COLUMN\_INFO

用于 [SORT\_INFO 结构](sort_info)。

typedef struct \_COLUMN\_INFO {

int iCol;

UINT nFlags;

} COLUMN\_INFO;

## 字段

_iCol_

指定要排序的列。

_nFlags_

指定下列值的组合。

|     |     |
| --- | --- |
| SORT\_ASCEND | 按升序排序。 |
| SORT\_DESCEND | 按降序排序。 |
| SORT\_DATE | 排序日期和时间。 |
| SORT\_LENGTH | 按文本长度排序。 |
| SORT\_NUM | 排序数字。 |
| SORT\_TEXT | 按字母顺序排序文本。 |
| SORT\_WORDS | 按字数排序文本。 |

## 版本

支持 EmEditor Professional Version 16.4 或之后的版本。
