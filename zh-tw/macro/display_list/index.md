# DisplayList 集合

DisplayList 集合提供 [DisplayItem 對象](../display_item/index) 的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索項目的總數。 |
| **[Item](item)** | 為指定索引檢索 [DisplayItem 對象](../display_item/index)。 |

## 示例

#### \[JavaScript\]

list = new Enumerator( document.Config.Display.ColorList );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.TextColor );

}

#### \[VBScript\]

For Each item In document.Config.Display.ColorList

alert item.TextColor

Next

## 版本

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:maxdepth: 1
count
item
```
