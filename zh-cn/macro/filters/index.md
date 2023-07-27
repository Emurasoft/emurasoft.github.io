# Filters 集合

Filters 集合提供 [Filter 对象](../filter/index) 的集合。

## 属性

|     |     |
| --- | --- |
|[Count](count) | 检索项目的数量。 |
|[Item](item) | 为指定的索引检索 [Filter 对象](../filter/index)。 |
|[VisibleLinesAbove](visible_lines_above) | 指定匹配行以上可见行的行数。 |
|[VisibleLinesBelow](visible_lines_below) | 指定匹配行以下可见行的行数。 |

## 方法

|     |     |
| --- | --- |
|[Add](add) | 添加一个项目。 |
|[AddFind](add_find) | 添加一个要搜索的项目。 |
|[AddReplace](add_replace) | 添加一个要替换的项目。 |
|[Clear](clear) | 删除集合中的所有项目。 |
|[Export](export) | 导出集合到 TSV 文件中。 |
|[Import](import) | 导入一个 TSV 文件到集合中。 |
|[Remove](remove) | 删除一个项目。 |

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

支持 EmEditor 16.0 或之后的版本。


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
