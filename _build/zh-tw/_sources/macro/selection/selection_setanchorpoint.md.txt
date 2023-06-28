# SetAnchorPoint 方法

設置選定內容的原點。

#### \[JavaScript\]

document.selection. **SetAnchorPoint**( _nFlags_, _xPos_, _yPos_
);

#### \[VBScript\]

document.selection. **SetAnchorPoint** _nFlags_, _xPos_, _yPos_

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

指定選定內容原點的列號。

_yPos_

指定選定內容原點的行號。

## 版本

支持 EmEditor 4.03 或之後的版本。