# SIZE\_PTR

Used to specify a size. In 32-bit plug-ins, SIZE\_PTR is the same as the SIZE structure. In 64-bit plug-ins, each field is extended to the 64-bit integer from the 32-bit integer.

typedef struct tagSIZE\_PTR

{

LONG\_PTR cx;

LONG\_PTR cy;

} SIZE\_PTR, \*PSIZE\_PTR;

## Fields

_x_

Specifies an x-axis value.

y

Specifies a y-axis value.
