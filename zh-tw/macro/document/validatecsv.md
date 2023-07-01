# ValidateCsv 方法 (Document ��H)

驗證 CSV 文檔和輸出錯誤，并可選擇調整分隔符位置。

#### \[JavaScript\]

_nResults_ = document. **ValidateCsv**( _nFlags_ );

#### \[VBScript\]

_nResults_ = document. **ValidateCsv**( _nFlags_ )

## 參數

_nFlags_

指定以下值的組合。 如果省略，將不指定任何標志。

|     |     |
| --- | --- |
| eeValidateAdjustColumns | 調整列寬。 |
| eeValidateAdjustEnlargeOnly | 與 **eeValidateAdjustColumns** 合用時，不能縮小，但只能擴大欄寬。 |
| eeValidateAdjustVisibleOnly | 與 eeValidateAdjustColumns 合用，僅調整可見行的分隔符位置。 |
| eeValidateDetectNL | 如果對目前的 [CSV 格式](../../dlg/customize/csv/index) 啟用 **允許換行符號在雙引號內**，這個標志會找到兩行，每行包含一個不成對的雙引號，並將這些雙引號之間的任何換行符號轉換為嵌入的換行符。 |
| eeValidateDontClearOutput | 不使用。 |
| eeValidateQuiet | 不在輸出欄中顯示任何信息或錯誤。 |
| eeValidateQuietIfNoError | 如果沒有錯誤，不在輸出欄中顯示任何信息。 |

## 返回值

返回值可以是以下值的組合。返回值為 0 表示沒有錯誤。

|     |     |
| --- | --- |
| eeCsvAbort | 操作被使用者中止。 |
| eeCsvAdjusted | 調整分隔符位置。 |
| eeCsvInconsistentColumns | 檢測到不一致的欄數。 |
| eeCsvInvalidQuotes | 檢測到無效的引號。 |
| eeCsvNLEmbedded | 無效的換行代碼嵌入到儲存格中。 |
| eeCsvNotCsv | 未選擇 CSV 模式。 |

## 示例

#### \[JavaScript\]

nResults = document.ValidateCsv( eeValidateQuiet );

if( nResults != 0 ) {

if( nResults & eeCsvAbort ) {

alert( "The operation was aborted by the user." );

}

if( nResults & eeCsvAdjusted ) {

alert( "Separator potisions were adjusted." );

}

if( nResults & eeCsvInconsistentColumns ) {

alert( "The inconsistent number of columns was detected." );

}

if( nResults & eeCsvInvalidQuotes ) {

alert( "An invalid quotation mark was detected." );

}

if( nResults & eeCsvNLEmbedded ) {

alert( "A newline code was embedded into a cell." );

}

if( nResults & eeCsvNotCsv ) {

alert( "A CSV mode was not selected." );

}

}

else {

alert( "There were no errors" );

}

#### \[VBScript\]

nResults = document.ValidateCsv( eeValidateQuiet )

If nResults <> 0 Then

If nResults And eeCsvAbort Then

alert( "The operation was aborted by the user." )

End If

If nResults And eeCsvAdjusted Then

alert( "Separator potisions were adjusted." )

End If

If nResults And eeCsvInconsistentColumns Then

alert( "The inconsistent number of columns was detected." )

End If

If nResults And eeCsvInvalidQuotes Then

alert( "An invalid quotation mark was detected." )

End If

If nResults & eeCsvNLEmbedded Then

alert( "A newline code was embedded into a cell." )

End If

If nResults & eeCsvNotCsv Then

alert( "A CSV mode was not selected." )

End If

Else

alert( "There were no errors" )

End If

## 版本

支持 EmEditor Professional Version 17.2 或之後的版本。
