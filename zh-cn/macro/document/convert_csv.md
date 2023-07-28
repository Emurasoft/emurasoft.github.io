# ConvertCsv 方法 (Document 对象)

转换 CSV 格式。

## 

### \[JavaScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

### \[VBScript\]

```
document.ConvertCsv( iDestMode, nFlags, strSepPos );
```

## 参数

_iDestMode_

指定要将当前文档转换为 CSV 格式的索引。0 表示固定宽度的列格式（非 CSV）。1 表示“自定义”对话框中 “CSV” 页面上的第一个定义的格式（默认情况下是“逗号分隔”）。

_nFlags_

你能指定一个下列值的组合。

| 值 | 含义 |
| --- | --- |
| eeCsvHalfWidth | 假定所有字符为半角字符以提高速度。 |
| eeCsvDiscardUndo | 丢弃撤消信息以提高速度。 |

_strSepCount_

如果当前文档是非 CSV 文档，并且要将当前固定列宽的文档转换为 CSV 文档，则此字符串指定分隔符之间的宽度，以逗号分隔。例如，“10，8” 表示 2 个以 10 和 8 个半角字符分隔的分隔符。如果当前文档是 CSV 文档，则忽略此参数。

## 示例

以下示例将固定宽度的列转换为逗号分隔的 CSV 格式。原始的固定列宽格式为：

Madrid Spain   100

Paris  France  101

目标 CSV 文档会变为：

Madrid,Spain,100

Paris,France,101

### \[JavaScript\]

```
document.ConvertCsv( 1, 0, "7,8" );
```

### \[VBScript\]

```
document.ConvertCsv 1, 0, "7,8"
```

## 版本

支持 EmEditor Professional 19.8 或之后的版本。
