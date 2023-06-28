# NoWrapList コレクション

NoWrapList コレクションは [NoWrapItem オブジェクト](../no_wrap_item/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | アイテムの数を取得します。 |
| **[Item](item)** | 指定したインデックスの [NoWrapItem オブジェクト](../no_wrap_item/index) を取得します。 |

## メソッド

|     |     |
| --- | --- |
| **[Add](add)** | アイテムを追加します。 |
| **[Remove](remove)** | アイテムを削除します。 |

## 例

#### \[JavaScript\]

list = new Enumerator( document.Config.NoWrap.List );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Name );

}

#### \[VBScript\]

For Each item In document.Config.NoWrap.List

alert item.Name

Next

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。

```{toctree}
:maxdepth: 1
add
count
item
remove
```
