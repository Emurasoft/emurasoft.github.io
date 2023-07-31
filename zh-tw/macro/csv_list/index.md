# CsvList 集合

CsvList 集合提供 [**Csv** 對象](../csv/index) 的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索 Csv 對象的數目。 |
| **[Item](item)** | 檢索指定索引的 [**Csv** 對象](../csv/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一個項目。 |
| [**Insert**](insert) | 插入一個項目。 |
| **[Remove](remove)** | 刪除一個項目。 |
| [**Reset**](reset) | 將集合重設為預設值。 |

## 範例

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

支持 EmEditor 19.4 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
add
count
insert
item
remove
reset
```
