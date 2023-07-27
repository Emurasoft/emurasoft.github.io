# Saved Property (Document Object)

Retrieves or sets the flag indicating whether the document is changed since
the last time it was saved or opened.

## 

### \[JavaScript\]

```
bSaved = document.Saved;
document.Saved = bSaved;
```

### \[VBScript\]

```
bSaved = document.Saved
document.Saved = bSaved
```

## Examples

### \[JavaScript\]

```
if( document.Saved )  alert( "The document is not changed." );
else  alert( "The document is changed." );
```

### \[VBScript\]

```
If document.Saved Then
alert( "The document is not changed." )
Else
alert( "The document is changed." )
End If
```

## Version

Supported on EmEditor Professional Version 4.00 or later.
