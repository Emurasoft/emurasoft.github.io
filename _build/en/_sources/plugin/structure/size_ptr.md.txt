# SIZE\_PTR

用來指定一個大小。在 32 位外掛程式中，SIZE\_PTR 與 SIZE 結構相同。在 64 位外掛程式中，每一個欄位都從 32 位整數被延伸到 64 位整數。

typedef struct tagSIZE\_PTR

{

LONG\_PTR cx;

LONG\_PTR cy;

} SIZE\_PTR, \*PSIZE\_PTR;

## 欄位

_x_

> 指定一個 x 軸值。

y

> 指定一個 y 軸值。