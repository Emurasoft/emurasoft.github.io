# FontList Collection

FontList collection provides a collection of [FontItem objects](../font_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [FontItem object](../font_item/index) for the specified index. |

## Examples

#### \[JavaScript\]

list = new Enumerator( document.Config.Font.DisplayList );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Name );

}

#### \[VBScript\]

For Each item In document.Config.Font.DisplayList

alert item.Name

Next

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:maxdepth: 1
count
item
```
