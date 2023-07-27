# REARRANGE\_COLUMNS\_INFO

[EE\_REARRANGE\_COLUMNS メッセージ](../message/ee_rearrange_columns) で使用します。

typedef struct \_REARRANGE\_COLUMNS\_INFO {

UINT cbSize;

UINT nColumnArraySize;

const INT\* piColumn;

} REARRANGE\_COLUMNS\_INFO;

## フィールド

_cbSize_

このデータ構造体のサイズ、sizeof( REARRANGE\_COLUMNS\_INFO )を指定します。

_nSize_

_piColumn_ フィールドに指定する列の数を指定します。

_piColumn_

再配置する列の順番を示す整数の配列を指定します。例えば、「0, 2, 4」は、元の CSV 文書の 1番目、3番目、5番目の列を結果に含めることを示します。

## バージョン

Version 22.1 以上で利用できます。
