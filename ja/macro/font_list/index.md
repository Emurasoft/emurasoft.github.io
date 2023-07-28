# FontList コレクション

FontList コレクションは [FontItem オブジェクト](../font_item/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | アイテムの数を取得します。 |
| **[Item](item)** | 指定したインデックスの [FontItem オブジェクト](../font_item/index) を取得します。 |

## 例

### \[JavaScript\]

```
list = new Enumerator( document.Config.Font.DisplayList );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Font.DisplayList
alert item.Name
Next
```

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。


```{toctree}
:maxdepth: 1
count
item
```
