# FindWindow Method (Shell Object)

Finds the top-level [Window object](../window/index) by a class name and/or by a window title.

#### \[JavaScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ )

## Parameters

_strClass_

Specifies the window's class name. If this parameter is empty, all class names match.

_strCaption_

Specifies the window name (title). If this parameter is empty, all window names match.

## Examples

#### \[JavaScript\]

wnd = shell.FindWindow( "", "Calculator" );

wnd.SetForeground();

#### \[VBScript\]

wnd = shell.FindWindow( "", "Calculator" )

wnd.SetForeground

## Version

Supported on EmEditor Professional Version 7.00 or later.