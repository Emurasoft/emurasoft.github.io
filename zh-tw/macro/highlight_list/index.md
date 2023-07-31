# HighlightList 集合

HighlightList 集合提供 [HighlightItem 對象](../highlight_item/index) 的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索項目總數。 |
| **[Item](item)** | 為指定索引檢索 [HighlightItem 對象](../highlight_item/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一個項目。 |
| **[Remove](remove)** | 刪除一個項目。 |

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

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
add
count
item
remove
```
