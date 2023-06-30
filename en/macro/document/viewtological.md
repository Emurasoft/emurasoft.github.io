# ViewToLogical Method (Document Object)

Convert the display coordinates of a specified position to the logical coordinates, and retrieves the position in the [**Point** object](../point/index).

#### \[JavaScript\]

_point_ = document. **ViewToLogical**( _x_, _y_ );

#### \[VBScript\]

_point_ = document. **ViewToLogical**( _x_, _y_ )

## Parameters

_x_

Specifies the one-based horizontal (character) position.

_y_

Specifies the one-based vertical (line) position.

## Examples

#### \[JavaScript\]

point = document.ViewToLogical( 10, 1 );

x = point.x;

y = point.y;

#### \[VBScript\]

point = document.ViewToLogical( 10, 1 )

x = point.x

y = point.y

## Version

Supported on EmEditor Professional Version 17.0 or later.