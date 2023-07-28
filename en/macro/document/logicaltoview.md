# LogicalToView Method (Document Object)

Converts the logical coordinates of a specified position to the display coordinates, and retrieves the position in the [**Point** object](../point/index).

## 

### \[JavaScript\]

```
point = document.LogicalView( x, y );
```

### \[VBScript\]

```
point = document.LogicalView( x, y )
```

## Parameters

_x_

Specifies the one-based horizontal (character) position.

_y_

Specifies the one-based vertical (line) position.

## Examples

### \[JavaScript\]

```
point = document.LogicalToView( 10, 1 );
x = point.x;
y = point.y;
```

### \[VBScript\]

```
point = document.LogicalToView( 10, 1 )
x = point.x
y = point.y
```

## Version

Supported on EmEditor Professional Version 17.0 or later.
