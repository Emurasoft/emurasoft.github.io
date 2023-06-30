# FindWindow 方法 (Shell ��H)

通過一個類名和/或視窗標題查找頂層 [Window 對象](../window/index)。

#### \[JavaScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wnd = shell. **FindWindow**( _strClass_, _strCaption_ )

## 參數

_strClass_

指定視窗類名。如果這個參數為空，所有類名都匹配。

_strCaption_

指定視窗名稱 (標題) 。如果該參數為空，所有視窗名稱都匹配。

## 示例

#### \[JavaScript\]

wnd = shell.FindWindow( "", "Calculator" );

wnd.SetForeground();

#### \[VBScript\]

wnd = shell.FindWindow( "", "Calculator" )

wnd.SetForeground

## 版本

支持 EmEditor 7.00 或之後的版本。