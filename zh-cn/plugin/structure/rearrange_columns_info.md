# REARRANGE\_COLUMNS\_INFO

用于 [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) 消息中。

typedef struct \_REARRANGE\_COLUMNS\_INFO {

UINT cbSize;

UINT nColumnArraySize;

const INT\* piColumn;

} REARRANGE\_COLUMNS\_INFO;

## 字段

_cbSize_

> 指定 sizeof( REARRANGE\_COLUMNS\_INFO )。

_nSize_

> 指定在 _piColumn_ 字段中指定的列数。

_piColumn_

> 指定一个整数数组，指示要重新排列的列的顺序。例如，"0, 2, 4" 表示结果将包括原始 CSV 文档的第一列、第三列和第五列。

## 版本

> 支持 EmEditor Professional v22.1 或之后的版本。
