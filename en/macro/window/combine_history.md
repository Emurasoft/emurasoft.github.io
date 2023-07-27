# CombineHistory Property (Window Object)

Specifies the undo/redo history to be combined or not combined.

## 

### \[JavaScript\]

```
b =CombineHistory;
CombineHistory = b;
```

### \[VBScript\]

```
b =CombineHistory
CombineHistory = b;
```

## Examples

### \[JavaScript\]

```
CombineHistory = true;
document.writeln( "ABC" );
document.writeln( "DEF" );
CombineHistory = false;
```

### \[VBScript\]

```
CombineHistory = True
document.writeln "ABC"
document.writeln "DEF"
CombineHistory = False
```

## Version

Supported on EmEditor Professional Version 15.5 or later.
