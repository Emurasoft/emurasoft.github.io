# Item Property (Windows Collection)

Retrieves the window object for the window of the specified index.

## 

### \[JavaScript\]

```
wnd = shell.windows.Item( Index );
```

### \[VBScript\]

```
wnd = shell.windows.Item( Index )
```

## Parameters

_Index_

Specifies the index of the window as a one-based integer.

## Examples

### \[JavaScript\]

```
alert( "Name of the first window: " + shell.windows.Item(1).Caption );
```

### \[VBScript\]

```
alert "Name of the first window: " + shell.windows.Item(1).Caption
```

## Version

Supported on EmEditor Professional Version 7.00 or later.
