# LogicalToView メソッド (Document オブジェクト)

論理座標を表示座標に変換します。

## 

### \[JavaScript\]

```
point = document.LogicalView( x, y );
```

### \[VBScript\]

```
point = document.LogicalView( x, y )
```

## パラメータ

_x_

1 を基底とする水平方向 (文字) の位置を指定します。

_y_

1 を基底とする垂直方向 (行) の位置を指定します。

## 例

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

## バージョン

EmEditor Professional Version 17.0 以上で利用できます。
