# NoWrapList Collection

NoWrapList collection provides a collection of [NoWrapItem objects](../no_wrap_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [NoWrapItem object](../no_wrap_item/index) for the specified index. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| **[Remove](remove)** | Removes an item. |

## Examples

#### \[JavaScript\]

list = new Enumerator( document.Config.NoWrap.List );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Name );

}

#### \[VBScript\]

For Each item In document.Config.NoWrap.List

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
