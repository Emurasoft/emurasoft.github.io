# HideQuotes Property (Document Object)

Sets or retrieves a flag indicating whether the Hide Quotes Temporarily mode is enabled in the CSV cell selection mode.

## 

### \[JavaScript\]

```
b = document.HideQuotes;
document.HideQuotes = b;
```

### \[VBScript\]

```
b = document.HideQuotes
document.HideQuotes = b
```

## Sample

### \[JavaScript\]

```
if( document.HideQuotes )  alert( "Hide Quotes Temporarily enabled." );
else  alert( "Hide Quotes Temporarily disabled." );
```

### \[VBScript\]

```
If document.HideQuotes Then
alert( "Hide Quotes Temporarily enabled." )
Else
alert( "Hide Quotes Temporarily disabled." )
End If
```

## Version

Supported on EmEditor Professional Version 20.7 or later.
