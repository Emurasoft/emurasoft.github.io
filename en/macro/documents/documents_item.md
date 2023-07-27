# Item Property (Documents Collection)

Retrieves the document object for the document of the specified index.

## 

### \[JavaScript\]

```
doc = editor.Documents.Item( Index );
```

### \[VBScript\]

```
doc = editor.Documents.Item( Index )
```

## Parameters

_Index_

Specifies the index of the document as a one-based integer.

## Examples

### \[JavaScript\]

```
alert( "Full Name for the first document: " + editor.Documents.Item(1).FullName );
```

### \[VBScript\]

```
alert "Full Name for the first document: " & editor.Documents.Item(1).FullName
```

## Version

Supported on EmEditor Professional Version 5.00 or later.
