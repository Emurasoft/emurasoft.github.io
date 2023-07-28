# MoveColumn 方法 (Document 对象)

在 CSV 模式下移动或复制指定列。

## 

### \[JavaScript\]

```
document.MoveColumn( iColumn, iColumn2, iColumnTo [ , nFlags ] );
```

### \[VBScript\]

```
document.MoveColumn iColumn, iColumn2, iColumnTo [ , nFlags ]
```

## 参数

_iColumn1_

指定要移动或复制的首列。

_iColumn2_

指定要移动或复制的最后一列。

_iColumnTo_

指定要把列移动或复制到其之前的列。

_nFlags_

你可以指定以下值之一。如果省略，则会用 eeColumnMove。

| 值 | 含义 |
| --- | --- |
| eeColumnMove | 把从 _iColumn1_ 到 _iColumn2_ 的列移动到 _iColumnTo_ 的列之前。 |
| eeColumnCopy | 把从 _iColumn1_ 到 _iColumn2_ 的列复制到 _iColumnTo_ 的列之前。 |

## 示例

以下示例将列 3 移动到最左边。

### \[JavaScript\]

```
document.MoveColumn( 3, 3, 1 );
```

### \[VBScript\]

```
document.MoveColumn 3, 3, 1
```

## 版本

支持 EmEditor Professional 19.7 或之后的版本。
