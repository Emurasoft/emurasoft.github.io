# CONVERT\_CSV\_INFO

用於 [EE\_CONVERT\_CSV](../message/ee_convert_csv) 消息。

```
typedef struct _CONVERT_CSV_INFO {
	UINT cbSize;
	int iDestMode;
	UINT nFlags;
	int nSepCount;
	const int* pcxSepWidths;
} CONVERT_CSV_INFO;
```

## 欄位

_cbSize_

指定 sizeof( CONVERT\_CSV\_INFO )。

_iDestMode_

指定要將目前的文檔轉換為 CSV 格式的索引。0 表示固定寬度的欄格式（非 CSV）。1 表示「自訂」對話方塊中 「CSV」 頁面上的第一個定義的格式（預設情況下是「逗號分隔」）。

_nFlags_

你能指定一個以下值的組合。

| 值 | 含義 |
| --- | --- |
| CSV\_HALF\_WIDTH | 假定所有字元為半形字元以提高速度。 |
| CSV\_DISCARD\_UNDO | 丟棄復原信息以提高速度。 |

_nSepCount_

如果目前的文檔是非 CSV 文檔，並且要將目前的固定欄寬的文檔轉換為 CSV 文檔，則此參數指定分隔符號數，並且它必須與在 _pcxSepWidths_ 參數中指定的陣列大小相同。如果目前的文檔是 CSV 文檔，則可忽略此參數。

_pcxSepWidths_

如果 _nSepCount_ 參數不是零，則指定表示分隔符號之間的寬度的整數陣列。

## 版本

支持 EmEditor Professional 19.8 或之後的版本。
