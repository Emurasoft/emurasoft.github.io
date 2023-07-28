# GetActivePointX 方法 (Selection 對象)

返回游標位置處的列號。

## 

### \[JavaScript\]

```
xPos = document.selection.GetActivePointX( nFlags [, iSel ] );
```

### \[VBScript\]

```
xPos = document.selection.GetActivePointX( nFlags [, iSel ] )
```

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eePosView | 返回列位置。 |
| eePosLogical | 從先前的新行 (或如果是第一行的話，就是文檔的開頭) 返回字元數。 |
| eePosLogicalA | 與 eePosLogical 相同，但把一個全形字元計為 2。 |
| eePosCell | CSV 儲存格單位 |

_iSel_

可選項。指定選定內容的索引，以 1 為基準。如果指定 0 或省略，會指定標準選擇。如果指定 1 或更大值，則 _nFlags_ 參數必須為 eePosLogical。

## 版本

支持 EmEditor 4.00 或之後的版本。
