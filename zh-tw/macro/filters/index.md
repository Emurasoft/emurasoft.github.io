# Filters 集合

Filters 集合提供 [Filter 對象](../filter/index) 的集合。

## 屬性

|     |     |
| --- | --- |
|[Count](count) | 檢索項目的數量。 |
|[Item](item) | 為指定的索引檢索 [Filter 對象](../filter/index)。 |
|[VisibleLinesAbove](visible_lines_above) | 指定符合行以上可見行的行數。 |
|[VisibleLinesBelow](visible_lines_below) | 指定符合行以下可見行的行數。 |

## 方法

|     |     |
| --- | --- |
|[Add](add) | 添加一個項目。 |
|[AddFind](add_find) | 添加一個要搜索的項目。 |
|[AddReplace](add_replace) | 添加一個要取代的項目。 |
|[Clear](clear) | 刪除集合中的所有項目。 |
|[Export](export) | 導出集合到 TSV 檔案中。 |
|[Import](import) | 導入一個 TSV 檔案到集合中。 |
|[Remove](remove) | 刪除一個項目。 |

## Examples

### \[JavaScript\]

```
list = new Enumerator( document.filters );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Value );
}
```

### \[VBScript\]

```
For Each item In document.filters
alert item.Value
Next
```

## 版本

支持 EmEditor 16.0 或之後的版本。


```{toctree}
:maxdepth: 1
add
add_find
add_replace
clear
count
export
import
item
remove
visible_lines_above
visible_lines_below
```
