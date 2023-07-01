# SIZE\_PTR

用来指定一个大小。在 32 位插件中，SIZE\_PTR 与 SIZE 结构相同。在 64 位插件中，每一个字段都从 32 位整数被延伸到 64 位整数。

typedef struct tagSIZE\_PTR

{

LONG\_PTR cx;

LONG\_PTR cy;

} SIZE\_PTR, \*PSIZE\_PTR;

## 字段

_x_

> 指定一个 x 轴值。

y

> 指定一个 y 轴值。
