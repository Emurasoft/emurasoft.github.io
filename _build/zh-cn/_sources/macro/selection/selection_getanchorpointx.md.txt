# GetAnchorPointX 方法

返回选定内容原点的列号。

#### \[JavaScript\]

xPos = document.selection. **GetAnchorPointX**( _nFlags_ );

#### \[VBScript\]

xPos = document.selection. **GetAnchorPointX**( _nFlags_ )

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eePosView | 返回列位置。 |
| eePosLogical | 从先前的新行（或如果是第一行的话，就是文档的开头）返回字符数。 |
| eePosLogicalA | 与 eePosLogical 相同，但把一个全角字符计为 2。 |
| eePosCell | CSV 单元格单位 |

## 版本

支持 EmEditor 4.03 或之后的版本。