# GetLine 方法 (Document ��H)

檢索指定行上的文字。

#### \[JavaScript\]

_str_ = document. **GetLine**( _yLine_ \[, _nFlags_ \] );

#### \[VBScript\]

_str_ = document. **GetLine**( _yLine_ \[, _nFlags_ \] )

## 參數

_yLine_

指定要一個檢索的文字的行號。Specifies a line number of the text to retrieve.

_nFlags_

可選項。您能從如下值中指定一個組合。如果您不指定任何值，EmEditor 會預設指定沒有返回代碼的邏輯坐標。

|     |     |
| --- | --- |
| eeGetLineView | 在視圖中指定坐標。 |
| eeGetLineWithNewLines | 添加返回代碼到文字中。 |

## 版本

支持 EmEditor 7.00 或之後的版本。