# DroppedFiles コレクション

DroppedFiles コレクションはフレーム ウィンドウにドロップされたファイル名のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
|[Count](count) | ドロップされたファイルの数を取得します。 |
|[Item](item) | 指定したインデックスのドロップされたファイル名を取得します。 |

## 例

### \[JavaScript\]

```
files = new Enumerator( DroppedFiles );
for( ; !files.atEnd(); files.moveNext() ){
alert( files.item() );
}
```

### \[VBScript\]

```
For Each str In DroppedFiles
alert str
Next
```

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。


```{toctree}
:maxdepth: 1
count
item
```
