# SerialToLogical メソッド (Document オブジェクト)

シリアル位置を論理座標に変換します。

## 

### \[JavaScript\]

```
point = document.SerialToLogical( nSerialPos );
```

### \[VBScript\]

```
point = document.SerialToLogical( nSerialPos )
```

## パラメータ

_nSerialPos_

シリアル位置を指定します。シリアル位置は、1を基底とするテキスト全体の最初からの文字位置です。

## 例

### \[JavaScript\]

```
point = document.SerialToLogical( 10 );
x = point.x;
y = point.y;
```

### \[VBScript\]

```
point = document.SerialToLogical( 10 )
x = point.x
y = point.y
```

## バージョン

EmEditor Professional Version 17.0 以上で利用できます。
