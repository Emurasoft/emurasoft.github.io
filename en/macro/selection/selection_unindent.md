# UnIndent Method (Selection Object)

Removes indents from the selected text by the specified number of
indentation levels.

## 

### \[JavaScript\]

```
document.selection.UnIndent( [ nCount ] );
```

### \[VBScript\]

```
document.selection.UnIndent [ nCount ]
```

## Parameters

_nCount_

Optional. Specifies the number of indentation
levels. The default is 1. If
negative, the method acts like the [**Indent**Method](selection_indent). If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.
