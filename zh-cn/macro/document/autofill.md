# AutoFill 方法 (Document 对象)

对 CSV 文档执行自动填充或快速填充操作。

## 

### \[JavaScript\]

```
nResults = document.AutoFill( xSrcCellStart, ySrcCellStart, xSrcCellEnd, ySrcCellEnd, xDestCellStart, yDestCellStart, xDestCellEnd, yDestCellEnd, nFlags, nIncrement );
```

### \[VBScript\]

```
nResults = document.AutoFill( xSrcCellStart, ySrcCellStart, xSrcCellEnd, ySrcCellEnd, xDestCellStart, yDestCellStart, xDestCellEnd, yDestCellEnd, nFlags, nIncrement )
```

## 参数

_xSrcCellStart_

指定源单元格起始位置的列号。

_ySrcCellStart_

指定源单元格起始位置的行号。

_xSrcCellEnd_

指定源单元格结束位置的列号。

_ySrcCellEnd_

指定源单元格结束位置的行号。

_xDestCellStart_

指定目标单元格起始位置的列号。

_yDestCellStart_

指定目标单元格起始位置的行号。

_xDestCellEnd_

指定目标单元格结束位置的列号。

_yDestCellEnd_

指定目标单元格结束位置的行号。

_nFlags_

指定一个下列值的组合。如果省略，将会自动指定 **eeFillDefault**。

|     |     |
| --- | --- |
| eeFillDefault | EmEditor 决定填充到目标单元格的值。 |
| eeFillCopy | 将源范围中的值复制到目标范围，必要时重复。 |
| eeFillSeries | 将源范围中的值作为一序列扩展到目标范围。 |
| eeFlashFill | 执行快速填充操作，即根据检测到的模式将源范围内的值扩展到目标范围。该标志仅适用于垂直方向。 |
| eeFillDontOverwrite | 自动填充操作不会改写目标范围中的现有单元格。不能与 eeFlashFill 结合使用。 |
| eeFillRepeat | 自动填充操作将在非空单元格上重复显示新的值。不能与 eeFlashFill 结合使用。 |

_nIncrement_

如果源范围只指定了一个单元格，并且 **eeFillSeries** 被指定为 _nFlags_ 的参数，那么可以在这指定序列的增量数。如果省略，将指定 1。

## 返回值

返回值为 0 意味着没有错误。返回值为 1 意味着消息无法检测到模式以完成自动填充或快速填充操作。

## 示例

### \[JavaScript\]

```
nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries | eeFillDontOverwrite );
if( nResults == 0 ) {
alert( "Success" );
}
```

### \[VBScript\]

```
nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries Or eeFillDontOverwrite );
If nResults == 0 Then
alert "Success"
End If
```

## 版本

支持 EmEditor 17.5 或之后的版本。
