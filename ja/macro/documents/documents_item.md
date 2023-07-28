# Item プロパティ (Documents コレクション)

指定するインデックスの文書の Document オブジェクトを取得します。

## 

### \[JavaScript\]

```
doc = editor.Documents.Item( Index );
```

### \[VBScript\]

```
doc = editor.Documents.Item( Index )
```

## パラメータ

_Index_

文書のインデックスを 1 を基底とする整数で指定します。

## 例

### \[JavaScript\]

```
alert( "最初の文書のフルパス: " + editor.Documents.Item(1).FullName );
```

### \[VBScript\]

```
alert "最初の文書のフルパス: " & editor.Documents.Item(1).FullName
```

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。
