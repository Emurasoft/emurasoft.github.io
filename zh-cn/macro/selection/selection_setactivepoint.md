# SetActivePoint 方法 (Selection ����)

设置关闭位置。

#### \[JavaScript\]

document.selection. **SetActivePoint**( _nFlags_, _xPos_, _yPos_\[, _bExtend_ \[ \[, _bExtend_ \] , iSel \] );

#### \[VBScript\]

document.selection. **SetActivePoint** _nFlags_, _xPos_, _yPos_\[, _bExtend_ \[ \[, _bExtend_ \] , iSel \]

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eePosView | 按视图中的列位置以及行号指定。 |
| eePosLogical | 按从先前的新行（或如果是第一行的话，就是文档的开头）计起的字符和行数。 |
| eePosLogicalA | 与 eePosLogical 相同，但把一个全角字符计为 2。 |
| eePosCellLogical | 逻辑坐标中的 CSV 单元格单位。 |
| eePosCellView | 显示坐标中的 CSV 单元格单位。 |

_xPos_

指定光标位置的列号。

_yPos_

指定光标位置的行号。

_bExtend_

可选项。决定是否要扩展当前选区。如果 _bExtend_ 是
true，那么选区的活动端会移动到要扩展的地方，而定位端则保留在它原来的位置。不然，两端都被移动到指定的位置。

_iSel_

可选项。指定选定内容的索引，以 1 为基准。如果 0 被指定或省略，会指定标准选择。如果指定 1 或更大值，则 _nFlags_ 参数必须为 eePosLogical。

## 版本

支持 EmEditor 4.00 或之后的版本。
