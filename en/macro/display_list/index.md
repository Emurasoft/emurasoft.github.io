# DisplayList Collection

DisplayList collection provides a collection of [DisplayItem objects](../display_item/index).

## Properties

|     |     |
| --- | --- |
|[Count](count) | Retrieves the number of items. |
|[Item](item) | Retrieves the [DisplayItem object](../display_item/index) for the specified index. |

## Examples

### \[JavaScript\]

```
list = new Enumerator( document.Config.Display.ColorList );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.TextColor );
}
```

### \[VBScript\]

```
For Each item In document.Config.Display.ColorList
alert item.TextColor
Next
```

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:maxdepth: 1
count
item
```
