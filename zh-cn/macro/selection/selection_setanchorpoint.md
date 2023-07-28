# SetAnchorPoint 方法 (Selection 对象)

设置选定内容的原点。

## 

### \[JavaScript\]

```
document.selection.SetAnchorPoint( nFlags, xPos, yPos
);
```

### \[VBScript\]

```
document.selection.SetAnchorPoint nFlags, xPos, yPos
```

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

指定选定内容原点的列号。

_yPos_

指定选定内容原点的行号。

## 版本

支持 EmEditor 4.03 或之后的版本。
