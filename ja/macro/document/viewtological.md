# ViewToLogical メソッド (Document オブジェクト)

表示座標を論理座標に変換します。

## 

### \[JavaScript\]

```
point = document.ViewToLogical( x, y );
```

### \[VBScript\]

```
point = document.ViewToLogical( x, y )
```

## パラメータ

_x_

1 を基底とする水平方向 (文字) の位置を指定します。

_y_

1 を基底とする垂直方向 (行) の位置を指定します。

## 例

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

## バージョン

EmEditor Professional Version 17.0 以上で利用できます。
