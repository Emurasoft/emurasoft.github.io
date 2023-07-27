# AutoFill 方法 (Document ��H)

對 CSV 文檔執行自動填滿或快速填入操作。

## 

### \[JavaScript\]

```
nResults = document.AutoFill( xSrcCellStart, ySrcCellStart, xSrcCellEnd, ySrcCellEnd, xDestCellStart, yDestCellStart, xDestCellEnd, yDestCellEnd, nFlags, nIncrement );
```

### \[VBScript\]

```
nResults = document.AutoFill( xSrcCellStart, ySrcCellStart, xSrcCellEnd, ySrcCellEnd, xDestCellStart, yDestCellStart, xDestCellEnd, yDestCellEnd, nFlags, nIncrement )
```

## 參數

_xSrcCellStart_

指定源儲存格起始位置的欄號。

_ySrcCellStart_

指定源儲存格起始位置的行號。

_xSrcCellEnd_

指定源儲存格結束位置的欄號。

_ySrcCellEnd_

指定源儲存格結束位置的行號。

_xDestCellStart_

指定目標儲存格起始位置的欄號。

_yDestCellStart_

指定目標儲存格起始位置的行號。

_xDestCellEnd_

指定目標儲存格結束位置的欄號。

_yDestCellEnd_

指定目標儲存格結束位置的行號。

_nFlags_

指定一個下列值的組合。如果省略，將會自動指定eeFillDefault。

|     |     |
| --- | --- |
| eeFillDefault | EmEditor 決定填充到目標儲存格的值。 |
| eeFillCopy | 將源範圍中的值複製到目標範圍，必要時重複。 |
| eeFillSeries | 將源範圍中的值作為一數列延伸到目標範圍。 |
| eeFlashFill | 執行快速填入操作，即根據檢測到的模式將源範圍內的值延伸到目標範圍。該標志僅適用於垂直方向。 |
| eeFillDontOverwrite | 自動填滿操作不會覆寫目標範圍中的現有儲存格。不能與 eeFlashFill 結合使用。 |
| eeFillRepeat | 自動填滿操作將在非空儲存格上重複顯示新的值。不能與 eeFlashFill 結合使用。 |

_nIncrement_

如果源範圍只指定了一個儲存格，並且eeFillSeries 被指定為 _nFlags_ 的參數，那么可以在這指定數列的增量數。如果省略，將指定 1。

## 返回值

返回值為 0 意味著沒有錯誤。返回值為 1 意味著消息無法檢測到模式以完成自動填滿或快速填入操作。

## 範例

### \[JavaScript\]

```
nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );
if( nResults == 0 ) {
alert( "Success" );
}
```

### \[VBScript\]

```
nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );
If nResults == 0 Then
alert "Success"
End If
```

## 版本

支持 EmEditor 17.5 或之後的版本。
