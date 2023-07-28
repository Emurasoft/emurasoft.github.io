# GetAnchorPointX 方法 (Selection 對象)

返回選定內容原點的列號。

## 

### \[JavaScript\]

```
xPos = document.selection.GetAnchorPointX( nFlags );
```

### \[VBScript\]

```
xPos = document.selection.GetAnchorPointX( nFlags )
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

## 版本

支持 EmEditor 4.03 或之後的版本。
