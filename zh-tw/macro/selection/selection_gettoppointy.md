# GetTopPointY 方法 (Selection ��H)

返回選定內容頂部的行號。

#### \[JavaScript\]

yPos = document.selection. **GetTopPointY**( _nFlags_ \[, _iSel_ \] );

#### \[VBScript\]

yPos = document.selection. **GetTopPointY**( _nFlags_ \[, _iSel_ \] )

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eePosView | 返回視圖中的行號。 |
| eePosLogical | 返回邏輯行號，取決于從文檔起始位置開始的新行數。 |
| eePosCellLogical | 邏輯坐標中的 CSV 儲存格單位。 |
| eePosCellView | 顯示坐標中的 CSV 儲存格單位。 |

_iSel_

可選項。指定選定內容的索引，以 1 為基準。如果 0 被指定或省略，會指定標準選擇。如果指定 1 或更大值，則 _nFlags_ 參數必須為 eePosLogical。

## 版本

支持 EmEditor 4.00 或之後的版本。