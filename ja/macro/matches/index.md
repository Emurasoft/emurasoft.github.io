# Matches コレクション

Matches コレクションは、正規表現の検索結果を表す [Match オブジェクト](../match/index) のコレクションを提供します。このコレクションは、最初のアイテムはマッチした全体のアイテム (後方参照 0) とサブ マッチ (後方参照 1, 2, 3, ...) から成り立ちます。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | Match オブジェクトの数を取得します。 |
| **[Item](item)** | 指定するインデックスの Match オブジェクトを取得します。Item(0) はマッチしたアイテム全体 (後方参照 0) を、Item(1) は後方参照 1 を返します。 |

## バージョン

EmEditor Professional Version 15.9 以上で利用できます。

```{toctree}
:hidden:
:maxdepth: 1
count
item
```