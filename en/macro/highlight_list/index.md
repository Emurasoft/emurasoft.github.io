# HighlightList Collection

HighlightList collection provides a collection of [HighlightItem objects](../highlight_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [HighlightItem object](../highlight_item/index) for the specified index. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| **[Remove](remove)** | Removes an item. |

## Examples

#### \[JavaScript\]

list = new Enumerator( document.Config.Highlight.List );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Name );

}

#### \[VBScript\]

For Each item In document.Config.Highlight.List

alert item.Name

Next

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:maxdepth: 1
add
count
item
remove
```
