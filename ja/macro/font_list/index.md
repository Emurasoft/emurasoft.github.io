# FontList コレクション

FontList コレクションは [FontItem オブジェクト](../font_item/index) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| **[Count](count)** | アイテムの数を取得します。 |
| **[Item](item)** | 指定したインデックスの [FontItem オブジェクト](../font_item/index) を取得します。 |

## 例

### \[JavaScript\]

次の例は、現在のフォントを "Consolas", 15 に設定します。

```
cfg = document.Config;
fontprop = cfg.Font;
displaylist = fontprop.DisplayList;
nCategory = document.FontCategory;
ft = displaylist.Item(nCategory + 1);
ft.Name = "Consolas";
ft.Size = 15;
ft.Bold = false;
ft.Italic = false;
cfg.Save();
```

次の例は、現在のフォントの名前とサイズを取得して表示します。

```
cfg = document.Config;
fontprop = cfg.Font;
displaylist = fontprop.DisplayList;
nCategory = document.FontCategory;
ft = displaylist.Item(nCategory + 1);
alert( ft.Name + ", " + ft.Size );
```

次の例は、各フォント カテゴリーに対するフォントを取得します。
The following retrieves the font for each font category.

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
:hidden:
:maxdepth: 1
count
item
```
