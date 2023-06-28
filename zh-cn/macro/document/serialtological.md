# SerialToLogical 方法

将串行位置转换为逻辑坐标，并检索在 [**Point** 对象](../point/index) 中的位置。

#### \[JavaScript\]

_point_ = document. **SerialToLogical**( _nSerialPos_ );

#### \[VBScript\]

_point_ = document. **SerialToLogical**( _nSerialPos_ )

## 参数

_nSerialPos_

指定串行位置，它是从整个文本开头的字符的基于一个索引。

## 示例

#### \[JavaScript\]

point = document.SerialToLogical( 10 );

x = point.x;

y = point.y;

#### \[VBScript\]

point = document.SerialToLogical( 10 )

x = point.x

y = point.y

## 版本

支持 EmEditor Professional 17.0 或之后的版本。