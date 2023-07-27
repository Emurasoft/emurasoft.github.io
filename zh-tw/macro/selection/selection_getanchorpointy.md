# GetAnchorPointY 方法 (Selection ��H)

返回選定內容原點的行號。

## 

### \[JavaScript\]

```
yPos = document.selection.GetAnchorPointY( nFlags );
```

### \[VBScript\]

```
yPos = document.selection.GetAnchorPointY( nFlags )
```

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eePosView | 返回視圖中的行號。 |
| eePosLogical | 返回邏輯行號，取決于從文檔起始位置開始的新行數。 |
| eePosCellLogical | 邏輯坐標中的 CSV 儲存格單位。 |
| eePosCellView | 顯示坐標中的 CSV 儲存格單位。 |

## 版本

支持 EmEditor 4.03 或之後的版本。
