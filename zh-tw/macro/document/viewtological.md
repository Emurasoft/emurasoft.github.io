# ViewToLogical 方法 (Document 對象)

將指定位置的顯示坐標轉換為邏輯坐標，并檢索 [**Point** 對象](../point/index) 中的位置。

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

指定基于單個的水平（字元）位置。

_y_

指定基于單個的垂直（行）位置。

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

## 版本

支持 EmEditor Professional 17.0 或之後的版本。
