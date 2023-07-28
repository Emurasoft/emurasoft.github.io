# Item Property (CsvList Collection)

Retrieves the [**Csv** object](../csv/index) of the specified index.

## 

### \[JavaScript\]

```
doc = editor.CsvList.Item( Index );
```

### \[VBScript\]

```
doc = editor.CsvList.Item( Index )
```

## Parameters

_Index_

Specifies the index of the Csv object as a one-based integer.

## Examples

### \[JavaScript\]

```
alert( "Name for the first Csv object: " + editor.CsvList.Item(1).Name );
```

### \[VBScript\]

```
alert "Name for the first Csv object: " & editor.CsvList.Item(1).Name
```

## Version

Supported on EmEditor Professional Version 19.4 or later.
