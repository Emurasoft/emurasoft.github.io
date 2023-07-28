# AUTOFILL\_INFO

用於 [EE\_AUTOFILL](../message/ee_autofill) 消息。

typedef struct \_AUTOFILL\_INFO {

UINT cbSize;

POINT\_PTR ptSrcCellStart;

POINT\_PTR ptSrcCellEnd;

POINT\_PTR ptDestCellStart;

POINT\_PTR ptDestCellEnd;

DWORD dwFlags;

INT64 nIncrement;

} AUTOFILL\_INFO;

## 成員

_cbSize_

以字節為單位的數據結構大小。在發送 [EE\_AUTOFILL](../message/ee_autofill) 消息之前，把這個成員設為 sizeof ( AUTOFILL\_INFO )。

_ptSrcCellStart_

指定源儲存格的起始位置。

_ptSrcCellEnd_

指定源儲存格的結束位置。

_ptDestCellStart_

指定目標儲存格的起始位置。

_ptDestCellEnd_

指定目標儲存格的結束位置。

_dwFlags_

指定一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FILL\_DEFAULT | EmEditor 決定填充到目標儲存格的值。 |
| FLAG\_FILL\_COPY | 將源範圍中的值複製到目標範圍，必要時重複。 |
| FLAG\_FILL\_SERIES | 將源範圍中的值作為一數列延伸到目標範圍。 |
| FLAG\_FILL\_FLASH | 執行快速填入操作，即根據檢測到的模式將源範圍內的值延伸到目標範圍。該標志僅適用於垂直方向。 |
| FLAG\_FILL\_DONT\_OVERWRITE | 自動填滿操作不會覆寫目標範圍中的現有儲存格。不能與 eeFlashFill 結合使用。 |
| FLAG\_FILL\_REPEAT | 自動填滿操作將在非空儲存格上重複顯示新的值。不能與 eeFlashFill 結合使用。 |

_nIncrement_

如果源範圍只指定了一個儲存格，並且 **FLAG\_FILL\_SERIES** 被指定為 _dwFlags_ 的參數，那么可以在這指定數列的增量數。

## 版本

支持 EmEditor 17.5 或之後的版本。
