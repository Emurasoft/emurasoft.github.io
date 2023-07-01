# CsvList Collection

CsvList collection provides a collection of [**Csv** objects](../csv/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of Csv objects. |
| **[Item](item)** | Retrieves the [**Csv** object](../csv/index) of the specified index. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| [**Insert**](insert) | Inserts an item. |
| **[Remove](remove)** | Removes an item. |
| [**Reset**](reset) | Resets the collection. |

## Examples

#### \[JavaScript\]

csvs = new Enumerator( editor.CsvList );

for( ; !csvs.atEnd(); csvs.moveNext() ){

item = csvs.item();

alert( item.Name );

}

#### \[VBScript\]

For Each item In editor.CsvList

alert item.Name

Next

## Version

Supported on EmEditor Professional Version 19.4 or later.


```{toctree}
:maxdepth: 1
add
count
insert
item
remove
reset
```
