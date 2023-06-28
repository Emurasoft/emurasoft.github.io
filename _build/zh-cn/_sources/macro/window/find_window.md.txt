# FindWindow 方法

通过类名和/或一个窗口标题查找子 [Window 对象](../window/index)。

#### \[JavaScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ )

## 参数

_strClass_

指定窗口的类名。如果此参数为空，所有类名相匹配。

_strCaption_

指定窗口名称（标题）。如果此参数为空，所有窗口名称相匹配。

## 示例

#### \[JavaScript\]

wnd = FindWindow( "EmEditorView", "" );

alert( wnd.Caption );

#### \[VBScript\]

wnd = FindWindow( "EmEditorView", "" )

alert wnd.Caption

## 版本

支持 EmEditor 7.00 或之后的版本。