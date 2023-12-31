# FindWindow Method (Window Object)

Finds the child [Window object](../window/index) by a class name and/or by a window title.

## 

### \[JavaScript\]

```
wndChild = wnd.FindWindow( strClass, strCaption );
```

### \[VBScript\]

```
wndChild = wnd.FindWindow( strClass, strCaption )
```

## Parameters

_strClass_

Specifies the window's class name. If this parameter is empty, all class names match.

_strCaption_

Specifies the window name (title). If this parameter is empty, all window names match.

## Examples

### \[JavaScript\]

```
wnd = FindWindow( "EmEditorView", "" );
alert( wnd.Caption );
```

### \[VBScript\]

```
wnd = FindWindow( "EmEditorView", "" )
alert wnd.Caption
```

## Version

Supported on EmEditor Professional Version 7.00 or later.
