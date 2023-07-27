# Import 方法 (Filters ���X)

把 TSV 檔案匯入到集合中。

## 

### \[JavaScript\]

```
list.Import( strFileName[, bAppend ] );
```

### \[VBScript\]

```
list.Import strFileName[, bAppend ]
```

## 參數

_strFileName_

指定包括 TSV 檔案的完整路徑的檔案名。

_bAppend_

指定方法是否匯入檔案并將篩選條件附加到現有篩選條件上。 如果省略，則假定為 False。

## 範例

### \[JavaScript\]

```
var filters = document.filters;
filters.Import( "E:\\\Test\\\filter.tsv" );
document.filters = filters;
```

### \[VBScript\]

```
Set filters = document.filters
filters.Import "E:\\Test\\filter.tsv"
document.filters = filters
```

## 版本

支持 EmEditor 16.0 或之後的版本。
