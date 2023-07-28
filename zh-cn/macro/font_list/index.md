# FontList 集合

FontList 集合提供 [FontItem 对象](../font_item/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索项目数量。 |
| **[Item](item)** | 为指定的索引检索 [FontItem 对象](../font_item/index)。 |

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

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:maxdepth: 1
count
item
```
