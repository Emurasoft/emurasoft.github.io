# Import Method (Filters Collection)

Imports a TSV file to the collection.

## 

### \[JavaScript\]

```
list.Import( strFileName[, bAppend ] );
```

### \[VBScript\]

```
list.Import strFileName[, bAppend ]
```

## Parameters

_strFileName_

Specifies the file name including the full path of the TSV file.

_bAppend_

Specifies whether the method imports a file and appends the filters to the existing filters. The False is assumed if omitted.

## Examples

### \[JavaScript\]

```
var filters = document.filters;
filters.Import( "E:\\Test\\filter.tsv" );
document.filters = filters;
```

### \[VBScript\]

```
Set filters = document.filters
filters.Import "E:\\Test\\filter.tsv"
document.filters = filters
```

## Version

Supported on EmEditor Professional Version 16.0 or later.
