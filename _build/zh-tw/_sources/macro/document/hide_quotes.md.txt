# HideQuotes 屬性

檢索或設定一個標志，該標志指示在 CSV 儲存格選擇模式下是否啟用了「隱藏引號」顯示畫面。

#### \[JavaScript\]

_b_ = document. **HideQuotes**;

document. **HideQuotes** = _b_;

#### \[VBScript\]

_b_ = document. **HideQuotes**

document. **HideQuotes** = _b_

## 範例

#### \[JavaScript\]

if( document.HideQuotes )  alert( "Unquoted/Unescaped View." );

else  alert( "Not Unquoted/Unescaped View." );

#### \[VBScript\]

If document.HideQuotes Then

alert( "Unquoted/Unescaped View." )

Else

alert( "Not Unquoted/Unescaped View." )

End If

## 版本

支持 EmEditor 20.7 或之後的版本。