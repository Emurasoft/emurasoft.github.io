# Import 方法 (Filters ����)

把 TSV 文件导入到集合中。

## 

### \[JavaScript\]

```
list.Import( strFileName[, bAppend ] );
```

### \[VBScript\]

```
list.Import strFileName[, bAppend ]
```

## 参数

_strFileName_

指定包括 TSV 文件的完整路径的文件名。

_bAppend_

指定方法是否导入文件并将筛选条件附加到现有筛选条件上。 如果省略，则假定为 False。

## 示例

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

支持 EmEditor 16.0 或之后的版本。
