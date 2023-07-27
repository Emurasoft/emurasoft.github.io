# SerialToLogical 方法 (Document ��H)

將串行位置轉換為邏輯坐標，并檢索在 [Point 對象](../point/index) 中的位置。

## 

### \[JavaScript\]

```
point = document.SerialToLogical( nSerialPos );
```

### \[VBScript\]

```
point = document.SerialToLogical( nSerialPos )
```

## 參數

_nSerialPos_

指定串行位置，它是從整個文字開頭的字元的基于一個索引。

## 範例

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

## 版本

支持 EmEditor Professional 17.0 或之後的版本。
