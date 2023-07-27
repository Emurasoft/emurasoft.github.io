# Export 方法 (Filters ����)

把集合导出到 TSV 文件中。

## 

### \[JavaScript\]

```
list.Export( strFileName );
```

### \[VBScript\]

```
list.Export strFileName
```

## 参数

_strFileName_

指定包括 TSV 文件的完整路径的文件名。

## 示例

### \[JavaScript\]

```
var filters = document.filters;
if( filters.Count > 0 ) {
filters.Export( "E:\\\Test\\\filter.tsv" );
}
```

### \[VBScript\]

```
Set filters = document.filters
If filters.Count > 0 Then
filters.Export "E:\\Test\\filter.tsv"
End If
```

## 版本

支持 EmEditor 16.0 或之后的版本。
