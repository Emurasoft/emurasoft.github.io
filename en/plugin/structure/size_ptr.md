# SIZE\_PTR

Used to specify a size. In 32-bit plug-ins, SIZE\_PTR is the same as the SIZE structure. In 64-bit plug-ins, each field is extended to the 64-bit integer from the 32-bit integer.

```
typedef struct tagSIZE_PTR {
	LONG_PTR cx;
	LONG_PTR cy;
} SIZE_PTR, *PSIZE_PTR;
```

## Fields

_x_

Specifies an x-axis value.

y

Specifies a y-axis value.
