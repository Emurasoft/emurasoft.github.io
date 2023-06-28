# ViewToLogical 方法

将指定位置的显示坐标转换为逻辑坐标，并检索 [**Point** 对象](../point/index) 中的位置。

#### \[JavaScript\]

_point_ = document. **ViewToLogical**( _x_, _y_ );

#### \[VBScript\]

_point_ = document. **ViewToLogical**( _x_, _y_ )

## Parameters

_x_

指定基于单个的水平（字符）位置。

_y_

指定基于单个的垂直（行）位置。

## Examples

#### \[JavaScript\]

point = document.ViewToLogical( 10, 1 );

x = point.x;

y = point.y;

#### \[VBScript\]

point = document.ViewToLogical( 10, 1 )

x = point.x

y = point.y

## 版本

支持 EmEditor Professional 17.0 或之后的版本。