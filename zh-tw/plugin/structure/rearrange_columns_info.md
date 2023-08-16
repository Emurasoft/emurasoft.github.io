# REARRANGE\_COLUMNS\_INFO

用於 [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) 消息中。

```
typedef struct _REARRANGE_COLUMNS_INFO {
	UINT cbSize;
	UINT nColumnArraySize;
	const INT* piColumn;
} REARRANGE_COLUMNS_INFO;
```

## 欄位

_cbSize_

指定 sizeof( REARRANGE\_COLUMNS\_INFO )。

_nSize_

指定在 _piColumn_ 欄位中指定的欄數。

_piColumn_

指定一個整數陣列，指示要重新排列的欄的順序。例如，"0, 2, 4" 表示結果將包括原始 CSV 文檔的第一欄、第三欄和第五欄。

## 版本

支持 EmEditor Professional v22.1 或之後的版本。
