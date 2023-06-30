# SetActivePoint 方法 (Selection ��H)

設置關閉位置。

#### \[JavaScript\]

document.selection. **SetActivePoint**( _nFlags_, _xPos_, _yPos_\[, _bExtend_ \[ \[, _bExtend_ \] , iSel \] );

#### \[VBScript\]

document.selection. **SetActivePoint** _nFlags_, _xPos_, _yPos_\[, _bExtend_ \[ \[, _bExtend_ \] , iSel \]

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eePosView | 按視圖中的列位置以及行號指定。 |
| eePosLogical | 按從先前的新行 (或如果是第一行的話，就是文檔的開頭) 計起的字元和行數。 |
| eePosLogicalA | 與 eePosLogical 相同，但把一個全形字元計為 2。 |
| eePosCellLogical | 邏輯坐標中的 CSV 儲存格單位。 |
| eePosCellView | 顯示坐標中的 CSV 儲存格單位。 |

_xPos_

指定游標位置的列號。

_yPos_

指定游標位置的行號。

_bExtend_

可選項。決定是否要延伸目前的選區。如果 _bExtend_ 是
true，那么選區的活動端會移動到要延伸的地方，而定位端則保留在它原來的位置。不然，兩端都被移動到指定的位置。

_iSel_

可選項。指定選定內容的索引，以 1 為基準。如果 0 被指定或省略，會指定標準選擇。如果指定 1 或更大值，則 _nFlags_ 參數必須為 eePosLogical。

## 版本

支持 EmEditor 4.00 或之後的版本。