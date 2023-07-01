# DroppedFiles Collection

DroppedFiles collection provides a collection of the names of dropped files in a frame window.

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of dropped files. |
| **[Item](item)** | Retrieves the file names for the dropped file of the specified index. |

## Examples

#### \[JavaScript\]

files = new Enumerator( DroppedFiles );

for( ; !files.atEnd(); files.moveNext() ){

alert( files.item() );

}

#### \[VBScript\]

For Each str In DroppedFiles

alert str

Next

## Version

Supported on EmEditor Professional Version 8.00 or later.


```{toctree}
:maxdepth: 1
count
item
```
