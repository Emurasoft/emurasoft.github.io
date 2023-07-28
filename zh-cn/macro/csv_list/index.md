# CsvList 集合

CsvList 集合提供 [**Csv** 对象](../csv/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索 Csv 对象的数目。 |
| **[Item](item)** | 检索指定索引的 [**Csv** 对象](../csv/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一个项目。 |
| [**Insert**](insert) | 插入一个项目。 |
| **[Remove](remove)** | 删除一个项目。 |
| [**Reset**](reset) | 将集合重置为默认值。 |

## 示例

### \[JavaScript\]

```
csvs = new Enumerator( editor.CsvList );
for( ; !csvs.atEnd(); csvs.moveNext() ){
item = csvs.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In editor.CsvList
alert item.Name
Next
```

## 版本

支持 EmEditor 19.4 或之后的版本。


```{toctree}
:maxdepth: 1
add
count
insert
item
remove
reset
```
