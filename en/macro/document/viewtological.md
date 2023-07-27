# ViewToLogical Method (Document Object)

Convert the display coordinates of a specified position to the logical coordinates, and retrieves the position in the [Point object](../point/index).

## 

### \[JavaScript\]

```
point = document.ViewToLogical( x, y );
```

### \[VBScript\]

```
point = document.ViewToLogical( x, y )
```

## Parameters

_x_

Specifies the one-based horizontal (character) position.

_y_

Specifies the one-based vertical (line) position.

## Examples

### \[JavaScript\]

```
point = document.ViewToLogical( 10, 1 );
x = point.x;
y = point.y;
```

### \[VBScript\]

```
point = document.ViewToLogical( 10, 1 )
x = point.x
y = point.y
```

## Version

Supported on EmEditor Professional Version 17.0 or later.
