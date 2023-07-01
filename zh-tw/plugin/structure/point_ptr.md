# POINT\_PTR

用來指定一個點的位置。在 32 位的外掛程式中，POINT\_PTR 與 POINT 結構相同。在 64 位外掛程式中，每一個欄位從 32 位整數被延伸到 64 位整數。

typedef struct tagPOINT\_PTR

{

LONG\_PTR x;

LONG\_PTR y;

} POINT\_PTR, \*PPOINT\_PTR;

## Fields

_x_

> 指定一個 x 軸值。

y

> 指定一個 y 軸值。
