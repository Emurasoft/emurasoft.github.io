# FontList 集合

FontList 集合提供 [FontItem 對象](../font_item/index) 的集合。

## 屬性

|     |     |
| --- | --- |
|[Count](count) | 檢索項目數量。 |
|[Item](item) | 為指定的索引檢索 [FontItem 對象](../font_item/index)。 |

## 示例

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

## 版本

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:maxdepth: 1
count
item
```
