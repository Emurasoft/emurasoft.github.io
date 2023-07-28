# AssociationList Collection

AssociationList collection provides a collection of [AssociationItem objects](../association_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [AssociationItem object](../association_item/index) for the specified index. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| **[Remove](remove)** | Removes an item. |

## Examples

### \[JavaScript\]

```
list = new Enumerator( document.Config.Association.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Association.List
alert item.Name
Next
```

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:maxdepth: 1
add
count
item
remove
```
