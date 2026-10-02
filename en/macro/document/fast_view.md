# FastView Property (Document Object)

Retrieves or sets whether the document is in Fast View mode.

## 

### \[JavaScript\]

```
bFastView = document.FastView;
document.FastView = bFastView;
```

### \[VBScript\]

```
bFastView = document.FastView
document.FastView = bFastView
```

## Remarks

Setting this property to **true** reopens the document in Fast View mode, and setting it to **false** reopens the document in normal mode, the same as the **Fast View** command. Nothing happens if the document is already in the specified mode.

This property can be set only for the active document. Setting this property fails if the document cannot be switched to the specified mode, for example, if the document is untitled.

While the document is opened in Fast View mode, subsequent macro calls on the document wait until EmEditor finishes reading the document.

## Examples

### \[JavaScript\]

```
if( document.FastView )  alert( "The document is in Fast View mode." );
else  alert( "The document is not in Fast View mode." );
document.FastView = true;
```

### \[VBScript\]

```
If document.FastView Then
alert( "The document is in Fast View mode." )
Else
alert( "The document is not in Fast View mode." )
End If
document.FastView = True
```

## Version

Supported on EmEditor Professional Version 26.3 or later.
