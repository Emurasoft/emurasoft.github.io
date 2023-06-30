# FindWindow 方法 (Shell ����)

通过一个类名和/或窗口标题查找顶层 [Window 对象](../window/index)。

#### \[JavaScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ )

## 参数

_strClass_

指定窗口类名。如果这个参数为空，所有类名都匹配。

_strCaption_

指定窗口名称（标题）。如果该参数为空，所有窗口名称都匹配。

## 示例

#### \[JavaScript\]

wnd = shell.FindWindow( "", "Calculator" );

wnd.SetForeground();

#### \[VBScript\]

wnd = shell.FindWindow( "", "Calculator" )

wnd.SetForeground

## 版本

支持 EmEditor 7.00 或之后的版本。