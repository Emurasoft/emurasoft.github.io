# POINT\_PTR

様々な座標を表すのに使用します。32 ビット用プラグインでは、POINT 構造体と同じ意味です。64 ビット用プラグインでは、各フィールドが 32 ビットから 64 ビットに拡張されます。

typedef struct tagPOINT\_PTR

{

LONG\_PTR x;

LONG\_PTR y;

} POINT\_PTR, \*PPOINT\_PTR;

## フィールド

_x_

> 水平方向の値を指定します。

_y_

> 垂直方向の値を指定します。
