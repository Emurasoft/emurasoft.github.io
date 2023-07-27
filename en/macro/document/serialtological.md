# SerialToLogical Method (Document Object)

Converts a serial position to the logical coordinates, and retrieves the position in the [Point object](../point/index).

## 

### \[JavaScript\]

```
point = document.SerialToLogical( nSerialPos );
```

### \[VBScript\]

```
point = document.SerialToLogical( nSerialPos )
```

## Parameters

_nSerialPos_

Specifies the serial position, which is one-based index of the character from the beginning of the entire text.

## Examples

### \[JavaScript\]

```
point = document.SerialToLogical( 10 );
x = point.x;
y = point.y;
```

### \[VBScript\]

```
point = document.SerialToLogical( 10 )
x = point.x
y = point.y
```

## Version

Supported on EmEditor Professional Version 17.0 or later.
