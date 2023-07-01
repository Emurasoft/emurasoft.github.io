# Filters Collection

Filters collection provides a collection of [Filter objects](../filter/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [Filter object](../filter/index) for the specified index. |
| **[VisibleLinesAbove](visible_lines_above)** | Specifies the number of visible lines above the matched lines. |
| **[VisibleLinesBelow](visible_lines_below)** | Specifies the number of visible lines below the matched lines. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| **[AddFind](add_find)** | Adds an item for a search. |
| **[AddReplace](add_replace)** | Adds an item for a replace. |
| **[Clear](clear)** | Removes all items in the collection. |
| **[Export](export)** | Exports the collection to a TSV file. |
| **[Import](import)** | Imports a TSV file to the collection. |
| **[Remove](remove)** | Removes an item. |

## Examples

#### \[JavaScript\]

list = new Enumerator( document.filters );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Value );

}

#### \[VBScript\]

For Each item In document.filters

alert item.Value

Next

## Version

Supported on EmEditor Professional Version 16.0 or later.


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
