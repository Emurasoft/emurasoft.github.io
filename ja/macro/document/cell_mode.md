# CellMode プロパティ (Document オブジェクト)

CSV セル選択モードかどうかを示すフラグを取得、または設定します。

## 

### \[JavaScript\]

```
b = document.CellMode;
document.CellMode = b;
```

### \[VBScript\]

```
b = document.CellMode
document.CellMode = b
```

## 例

### \[JavaScript\]

```
if( document.CellMode )  alert( "セル選択モードです" );
else  alert( "セル選択モードではありません" );
```

### \[VBScript\]

```
If document.CellMode Then
alert( "セル選択モードです" )
Else
alert( "セル選択モードではありません" )
End If
```

## バージョン

EmEditor Professional Version 15.8 以上で利用できます。
