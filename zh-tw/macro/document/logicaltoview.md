# LogicalToView 方法 (Document 對象)

將指定位置的邏輯坐標轉換為顯示坐標，并檢索 [**Point** 對象](../point/index) 中的位置。

## 

### \[JavaScript\]

```
point = document.LogicalView( x, y );
```

### \[VBScript\]

```
point = document.LogicalView( x, y )
```

## 參數

_x_

指定基于單個的水平（字元）位置。

_y_

指定基于單個的垂直（行）位置。

## 範例

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

## 版本

支持 EmEditor Professional 17.0 或之後的版本。
