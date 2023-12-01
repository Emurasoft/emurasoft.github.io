# FontList Collection

FontList collection provides a collection of [FontItem objects](../font_item/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of items. |
| **[Item](item)** | Retrieves the [FontItem object](../font_item/index) for the specified index. |

## Examples

### \[JavaScript\]

The following example sets the current font as "Consolas", 15.

```
cfg = document.Config;
fontprop = cfg.Font;
displaylist = fontprop.DisplayList;
nCategory = document.FontCategory;
ft = displaylist.Item(nCategory + 1);
ft.Name = "Consolas";
ft.Size = 15;
ft.Bold = false;
ft.Italic = false;
cfg.Save();
```

The following example retrieves and displays the current font name and size.

```
cfg = document.Config;
fontprop = cfg.Font;
displaylist = fontprop.DisplayList;
nCategory = document.FontCategory;
ft = displaylist.Item(nCategory + 1);
alert( ft.Name + ", " + ft.Size );
```

The following retrieves the font for each font category.

```
list = new Enumerator( document.Config.Font.DisplayList );
for( ; !list.atEnd(); list.moveNext() ){
    item = list.item();
    alert( item.Name );
}
```

### \[VBScript\]

The following retrieves the font for each font category.

```
For Each item In document.Config.Font.DisplayList
    alert item.Name
Next
```

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
