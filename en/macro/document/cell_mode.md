# CellMode Property (Document Object)

Sets or retrieves a flag indicating whether the selection mode is cell selection mode.

## 

### \[JavaScript\]

```
b = document.CellMode;
document.CellMode = b;
```

### \[VBScript\]

```
b = document.CellMode
document.CellMode = b
```

## Sample

### \[JavaScript\]

```
if( document.CellMode )  alert( "Cell selection mode." );
else  alert( "Not cell selection mode." );
```

### \[VBScript\]

```
If document.CellMode Then
alert( "Cell selection mode." )
Else
alert( "Not cell selection mode." )
End If
```

## Version

Supported on EmEditor Professional Version 15.8 or later.
