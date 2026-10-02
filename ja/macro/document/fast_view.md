# FastView プロパティ (Document オブジェクト)

文書が高速ビュー モードかどうかを取得、または設定します。

## 

### \[JavaScript\]

```
bFastView = document.FastView;
document.FastView = bFastView;
```

### \[VBScript\]

```
bFastView = document.FastView
document.FastView = bFastView
```

## 解説

このプロパティを **true** に設定すると、文書を高速ビュー モードで開き直し、**false** に設定すると、通常モードで開き直します。これは **高速ビュー** コマンドと同じです。文書がすでに指定するモードの場合は、何も行いません。

このプロパティは、アクティブな文書に対してのみ設定できます。文書を指定するモードに切り替えることができない場合、たとえば文書が無題の場合、設定は失敗します。

文書を高速ビュー モードで開いている間、その文書に対する以降のマクロの呼び出しは、EmEditor が文書の読み込みを完了するまで待機します。

## 例

### \[JavaScript\]

```
if( document.FastView )  alert( "文書は高速ビュー モードです" );
else  alert( "文書は高速ビュー モードではありません" );
document.FastView = true;
```

### \[VBScript\]

```
If document.FastView Then
alert( "文書は高速ビュー モードです" )
Else
alert( "文書は高速ビュー モードではありません" )
End If
document.FastView = True
```

## バージョン

EmEditor Professional Version 26.3 以上で利用できます。
