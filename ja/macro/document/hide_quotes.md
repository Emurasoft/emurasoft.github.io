# HideQuotes プロパティ ()

CSV セル選択モードで、一時的に引用符を非表示にするかどうかを示すフラグを取得、または設定します。

## 

### \[JavaScript\]

```
b = document.HideQuotes;
document.HideQuotes = b;
```

### \[VBScript\]

```
b = document.HideQuotes
document.HideQuotes = b
```

## 例

### \[JavaScript\]

```
if( document.HideQuotes )  alert( "一時的に引用符を非表示しています" );
else  alert( "一時的に引用符を非表示していません" );
```

### \[VBScript\]

```
If document.HideQuotes Then
alert( "一時的に引用符を非表示しています" )
Else
alert( "一時的に引用符を非表示していません" )
End If
```

## バージョン

EmEditor Professional Version 20.7 以上で利用できます。
