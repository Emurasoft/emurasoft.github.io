# Title Property (Document Object)

Retrieves or sets the title of the document. The title may contain long and short titles separated by a linefeed (\\n or Chr(10)).

## 

### \[JavaScript\]

```
strTitle = document.Title;document.Title = strTitle;
```

### \[VBScript\]

```
strTitle = document.Title document.Title = strTitle
```

## Examples

### \[JavaScript\]

```
document.Title = "This is a long title.\\nShort title";
```

### \[VBScript\]

```
document.Title = "This is a long title." & Chr(10) & "Short title"
```

## Version

Supported on EmEditor Professional Version 21.8 or later.
