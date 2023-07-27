# Documents コレクション

Documents コレクションは、フレーム ウィンドウに表示されている文書 ( [Document オブジェクト](../document/index)) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| [Count](documents_count) | 文書の数を取得します。 |
| [Item](documents_item) | 指定するインデックスの文書の Document オブジェクトを取得します。 |

## 例

### \[JavaScript\]

```
docs = new Enumerator( editor.Documents );
for( ; !docs.atEnd(); docs.moveNext() ){
doc = docs.item();
alert( doc.Name );
}
```

### \[VBScript\]

```
For Each doc In editor.Documents
alert doc.FullName
Next
```

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。


```{toctree}
:maxdepth: 1
documents_count
documents_item
```
