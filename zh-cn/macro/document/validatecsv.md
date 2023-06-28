# ValidateCsv 方法

验证 CSV 文档和输出错误，并可选择调整分隔符位置。

#### \[JavaScript\]

_nResults_ = document. **ValidateCsv**( _nFlags_ );

#### \[VBScript\]

_nResults_ = document. **ValidateCsv**( _nFlags_ )

## 参数

_nFlags_

指定以下值的组合。 如果省略，将不指定任何标志。

|     |     |
| --- | --- |
| eeValidateAdjustColumns | 调整列宽。 |
| eeValidateAdjustEnlargeOnly | 与 **eeValidateAdjustColumns** 合用时，不能缩小，但只能扩大列宽。 |
| eeValidateAdjustVisibleOnly | 与 eeValidateAdjustColumns 合用，仅调整可见行的分隔符位置。 |
| eeValidateDetectNL | 如果对当前 [CSV 格式](../../dlg/customize/csv/index) 启用 **允许换行符在双引号内**，这个标志会找到两行，每行包含一个不成对的双引号，并将这些双引号之间的任何换行符转换为嵌入的换行符。 |
| eeValidateDontClearOutput | 不使用。 |
| eeValidateQuiet | 不在输出栏中显示任何信息或错误。 |
| eeValidateQuietIfNoError | 如果没有错误，不在输出栏中显示任何信息。 |

## 返回值

返回值可以是以下值的组合。返回值为 0 表示没有错误。

|     |     |
| --- | --- |
| eeCsvAbort | 操作被用户中止。 |
| eeCsvAdjusted | 调整分隔符位置。 |
| eeCsvInconsistentColumns | 检测到不一致的列数。 |
| eeCsvInvalidQuotes | 检测到无效的引号。 |
| eeCsvNLEmbedded | 无效的换行代码嵌入到单元格中。 |
| eeCsvNotCsv | 未选择 CSV 模式。 |

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

支持 EmEditor Professional Version 17.2 或之后的版本。