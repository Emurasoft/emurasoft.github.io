# KeyboardList Collection

KeyboardList collection provides a collection of [KeyboardItem objects](../keyboard_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [KeyboardItem object](../keyboard_item/index) for the specified index. |

## Methods

|     |     |
| --- | --- |
| **[Add](add)** | Adds an item. |
| **[Remove](remove)** | Removes an item. |

## Examples

### \[JavaScript\]

```
list = new Enumerator( document.Config.Keyboard.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Key );
}
```

### \[VBScript\]

```
For Each item In document.Config.Keyboard.List
alert item.Key
Next
```

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
add
count
item
remove
```
