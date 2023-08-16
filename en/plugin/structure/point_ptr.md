# POINT\_PTR

Used to specify a point position. In 32-bit plug-ins, POINT\_PTR is the same as the POINT structure. In 64-bit plug-ins, each field is extended to the 64-bit integer from the 32-bit integer.

```
typedef struct tagPOINT_PTR {
	LONG_PTR x;
	LONG_PTR y;
} POINT_PTR, *PPOINT_PTR;
```

## Fields

_x_

Specifies an x-axis value.

y

Specifies a y-axis value.
