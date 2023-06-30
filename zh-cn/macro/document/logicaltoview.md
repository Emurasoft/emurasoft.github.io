# LogicalToView 方法 (Document ����)

将指定位置的逻辑坐标转换为显示坐标，并检索 [**Point** 对象](../point/index) 中的位置。

#### \[JavaScript\]

_point_ = document. **LogicalView**( _x_, _y_ );

#### \[VBScript\]

_point_ = document. **LogicalView**( _x_, _y_ )

## 参数

_x_

指定基于单个的水平（字符）位置。

_y_

指定基于单个的垂直（行）位置。

## 示例

#### \[JavaScript\]

point = document.LogicalToView( 10, 1 );

x = point.x;

y = point.y;

#### \[VBScript\]

point = document.LogicalToView( 10, 1 )

x = point.x

y = point.y

## 版本

支持 EmEditor Professional 17.0 或之后的版本。