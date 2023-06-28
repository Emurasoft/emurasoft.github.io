# AUTOFILL\_INFO

用于 [EE\_AUTOFILL](../message/ee_autofill) 消息。

typedef struct \_AUTOFILL\_INFO {

UINT cbSize;

POINT\_PTR ptSrcCellStart;

POINT\_PTR ptSrcCellEnd;

POINT\_PTR ptDestCellStart;

POINT\_PTR ptDestCellEnd;

DWORD dwFlags;

INT64 nIncrement;

} AUTOFILL\_INFO;

## 成员

_cbSize_

> 以字节为单位的数据结构大小。在发送 [EE\_AUTOFILL](../message/ee_autofill) 消息之前，把这个成员设为 sizeof ( AUTOFILL\_INFO )。

_ptSrcCellStart_

> 指定源单元格的起始位置。

_ptSrcCellEnd_

> 指定源单元格的结束位置。

_ptDestCellStart_

> 指定目标单元格的起始位置。

_ptDestCellEnd_

> 指定目标单元格的结束位置。

_dwFlags_

> 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FILL\_DEFAULT | EmEditor 决定填充到目标单元格的值。 |
> | FLAG\_FILL\_COPY | 将源范围中的值复制到目标范围，必要时重复。 |
> | FLAG\_FILL\_SERIES | 将源范围中的值作为一序列扩展到目标范围。 |
> | FLAG\_FILL\_FLASH | 执行快速填充操作，即根据检测到的模式将源范围内的值扩展到目标范围。该标志仅适用于垂直方向。 |
> | FLAG\_FILL\_DONT\_OVERWRITE | 自动填充操作不会改写目标范围中的现有单元格。不能与 eeFlashFill 结合使用。 |
> | FLAG\_FILL\_REPEAT | 自动填充操作将在非空单元格上重复显示新的值。不能与 eeFlashFill 结合使用。 |

_nIncrement_

> 如果源范围只指定了一个单元格，并且 **FLAG\_FILL\_SERIES** 被指定为 _dwFlags_ 的参数，那么可以在这指定序列的增量数。

## 版本

> 支持 EmEditor 17.5 或之后的版本。