# GetBottomPointX 方法 (Selection ����)

返回选定内容底部的列号。

#### \[JavaScript\]

xPos = document.selection. **GetBottomPointX**( _nFlags_ \[, _iSel_ \] );

#### \[VBScript\]

xPos = document.selection. **GetBottomPointX**( _nFlags_ \[, _iSel_ \] )

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eePosView | 返回列位置。 |
| eePosLogical | 从先前的新行（或如果是第一行的话，就是文档的开头）返回字符数。 |
| eePosLogicalA | 与 eePosLogical 相同，但把一个全角字符计为 2。 |

_iSel_

可选项。指定选定内容的索引，以 1 为基准。如果 0 被指定或省略，会指定标准选择。如果指定 1 或更大值，则 _nFlags_ 参数必须为 eePosLogical。

## 版本

支持 EmEditor 4.00 或之后的版本。
