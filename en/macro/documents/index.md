# Documents Collection

Documents collection provides a collection of document objects in a frame window.

## Properties

|     |     |
| --- | --- |
| **[Count](documents_count)** | Retrieves the number of documents. |
| **[Item](documents_item)** | Retrieves the document object for the document of the specified index. |

## Examples

### \[JavaScript\]

```
docs = new Enumerator( editor.Documents );
for( ; !docs.atEnd(); docs.moveNext() ){
doc = docs.item();
alert( doc.Name );
}
```

### \[VBScript\]

```
For Each doc In editor.Documents
alert doc.FullName
Next
```

## Version

Supported on EmEditor Professional Version 5.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
documents_count
documents_item
```
