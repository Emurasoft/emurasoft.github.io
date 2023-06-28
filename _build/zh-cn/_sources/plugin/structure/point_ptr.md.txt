# POINT\_PTR

用来指定一个点的位置。在 32 位的插件中，POINT\_PTR 与 POINT 结构相同。在 64 位插件中，每一个字段从 32 位整数被延伸到 64 位整数。

typedef struct tagPOINT\_PTR

{

LONG\_PTR x;

LONG\_PTR y;

} POINT\_PTR, \*PPOINT\_PTR;

## Fields

_x_

> 指定一个 x 轴值。

y

> 指定一个 y 轴值。