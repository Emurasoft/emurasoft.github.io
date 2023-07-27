# Export Method (Filters Collection)

Exports the collection to a TSV file.

## 

### \[JavaScript\]

```
list.Export( strFileName );
```

### \[VBScript\]

```
list.Export strFileName
```

## Parameters

_strFileName_

Specifies the file name including the full path of the TSV file.

## Examples

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

## Version

Supported on EmEditor Professional Version 16.0 or later.
