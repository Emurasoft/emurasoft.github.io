# HideQuotes 属性

检索或设置一个标志，该标志指示在 CSV 单元格选择模式下是否启用了“隐藏引号”视图。

#### \[JavaScript\]

_b_ = document. **HideQuotes**;

document. **HideQuotes** = _b_;

#### \[VBScript\]

_b_ = document. **HideQuotes**

document. **HideQuotes** = _b_

## 示例

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

支持 EmEditor 20.7 或之后的版本。