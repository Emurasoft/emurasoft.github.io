# Export 方法 (Filters 集合)

把集合匯出到 TSV 檔案中。

## 

### \[JavaScript\]

```
list.Export( strFileName );
```

### \[VBScript\]

```
list.Export strFileName
```

## 參數

_strFileName_

指定包括 TSV 檔案的完整路徑的檔案名。

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

支持 EmEditor 16.0 或之後的版本。
