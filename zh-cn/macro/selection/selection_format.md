# Format 方法 (Selection 对象)

插入或删除选定内容中的换行符。

## 

### \[JavaScript\]

```
document.selection.Format( nFlags );
```

### \[VBScript\]

```
document.selection.Format nFlags
```

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeFormatInsertNL | 在选区的换行处插入换行符。 |
| eeFormatDeleteNL | 在选区的换行处移除换行符。 |
| eeFormatSplitLines | 通过插入换行符并删除尾随空格来分割行（适用于 EmEditor 4.10 或之后的版本）。 |
| eeFormatJoinLines | 通过插入换行符并删除尾随空格来合并行（适用于 EmEditor 4.10 或之后的版本）。 |

## 版本

支持 EmEditor 4.00 或之后的版本。
