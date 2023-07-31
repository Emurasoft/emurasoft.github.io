# DisplayList 集合

DisplayList 集合提供 [DisplayItem 对象](../display_item/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索项目的总数。 |
| **[Item](item)** | 为指定索引检索 [DisplayItem 对象](../display_item/index)。 |

## 示例

### \[JavaScript\]

```
list = new Enumerator( document.Config.Display.ColorList );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.TextColor );
}
```

### \[VBScript\]

```
For Each item In document.Config.Display.ColorList
alert item.TextColor
Next
```

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
