# HighlightList 集合

HighlightList 集合提供 [HighlightItem 对象](../highlight_item/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索项目总数。 |
| **[Item](item)** | 为指定索引检索 [HighlightItem 对象](../highlight_item/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一个项目。 |
| **[Remove](remove)** | 删除一个项目。 |

## 示例

### \[JavaScript\]

```
list = new Enumerator( document.Config.Highlight.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Highlight.List
alert item.Name
Next
```

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:maxdepth: 1
add
count
item
remove
```
