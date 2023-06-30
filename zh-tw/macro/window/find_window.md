# FindWindow 方法 (Window ��H)

通過類名和/或一個視窗標題尋找子 [Window 對象](../window/index)。

#### \[JavaScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ )

## 參數

_strClass_

指定視窗的類名。如果此參數為空，所有類名相符合。

_strCaption_

指定視窗名稱 (標題) 。如果此參數為空，所有視窗名稱相符合。

## 示例

#### \[JavaScript\]

wnd = FindWindow( "EmEditorView", "" );

alert( wnd.Caption );

#### \[VBScript\]

wnd = FindWindow( "EmEditorView", "" )

alert wnd.Caption

## 版本

支持 EmEditor 7.00 或之後的版本。