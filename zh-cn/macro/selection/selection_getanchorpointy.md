# GetAnchorPointY 方法 (Selection 对象)

返回选定内容原点的行号。

## 

### \[JavaScript\]

```
yPos = document.selection.GetAnchorPointY( nFlags );
```

### \[VBScript\]

```
yPos = document.selection.GetAnchorPointY( nFlags )
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

## 版本

支持 EmEditor 4.03 或之后的版本。
