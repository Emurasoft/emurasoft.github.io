# Saved プロパティ ()

文書を前回保存または開いた後に変更されているかどうかを示すフラグを取得、または設定します。

#### \[JavaScript\]

_bSaved_ = document. **Saved**;

document. **Saved** = _bSaved_;

#### \[VBScript\]

_bSaved_ = document. **Saved**

document. **Saved** = _bSaved_

## 例

#### \[JavaScript\]

if( document.Saved )  alert( "文書は変更されていません" );

else  alert( "文書は変更されています" );

#### \[VBScript\]

If document.Saved Then

alert( "文書は変更されていません" )

Else

alert( "文書は変更されています" )

End If

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。