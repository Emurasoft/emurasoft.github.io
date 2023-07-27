# GetBottomPointY 方法 (Selection ����)

返回选定内容底部的行号。

## 

### \[JavaScript\]

```
yPos = document.selection.GetBottomPointY( nFlags [, iSel ] );
```

### \[VBScript\]

```
yPos = document.selection.GetBottomPointY( nFlags [, iSel ] )
```

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eePosView | 返回视图中的行号。 |
| eePosLogical | 返回逻辑行号，取决于从文档起始位置开始的新行数。 |
| eePosCellLogical | 逻辑坐标中的 CSV 单元格单位。 |
| eePosCellView | 显示坐标中的 CSV 单元格单位。 |

_iSel_

可选项。指定选定内容的索引，以 1 为基准。如果 0 被指定或省略，会指定标准选择。如果指定 1 或更大值，则 _nFlags_ 参数必须为 eePosLogical。

## 版本

支持 EmEditor 4.00 或之后的版本。
