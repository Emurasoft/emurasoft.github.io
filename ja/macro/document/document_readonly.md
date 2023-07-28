# ReadOnly プロパティ (Document オブジェクト)

文書が書き換え禁止状態かどうかを取得、または設定します。

## 

### \[JavaScript\]

```
bReadOnly = document.ReadOnly;
document.ReadOnly = bReadOnly;
```

### \[VBScript\]

```
bReadOnly = document.ReadOnly
document.ReadOnly = bReadOnly
```

## 例

### \[JavaScript\]

```
if( document.ReadOnly )  alert( "文書は書き換え禁止です" );
else  alert( "文書は書き換え禁止ではありません" );
```

### \[VBScript\]

```
If document.ReadOnly Then
alert( "文書は書き換え禁止です" )
Else
alert( "文書は書き換え禁止ではありません" )
End If
```

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
