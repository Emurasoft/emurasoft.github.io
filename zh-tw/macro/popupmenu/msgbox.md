# MsgBox 方法 (PopupMenu ��H)

根據對象提供的信息顯示對話方塊，並檢索所選按鈕、選項按鈕或命令連結的識別項。此方法忽略分隔項和子功能表。

#### \[JavaScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ );

#### \[VBScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ )

## 參數

_strMessage_

指定要顯示的消息。

_strMessage2_

可選。指定要在第一條消息下方顯示的附加消息。

_flags_

可選。指定以下值的組合。eeCommandLinks 和 eeRadioButtons 不能合用。

|     |     |
| --- | --- |
| eeCommandLinks | 指示功能表項將顯示為命令連結而不是按鈕。 |
| eeRadioButtons | 指示功能表項將顯示為選項按鈕而不是按鈕。 |
| eeHideStopMacro | 從對話方塊中隱藏停止巨集核取方塊。 |
| eeIconStop | 對話方塊中出現一個停止標志圖示。 |
| eeIconExclamation | 對話方塊中出現一個感嘆號圖示。 |
| eeIconInformation | 對話方塊中出現一個由圓圈中的小寫字母 i 組成的圖示。 |

## 範例

#### \[JavaScript\]

menu = CreatePopupMenu();

menu.Add( "Button 1", 1, eeMenuChecked );

menu.Add( "Button 2", 2 );

result = menu.MsgBox( "Header", "Body", eeIconInformation );

if( result != 0 ) alert( menu.GetText( result ) );

result = menu.MsgBox( "Header", "Body", eeCommandLinks \| eeIconExclamation );

if( result != 0 ) alert( menu.GetText( result ) );

result = menu.MsgBox( "Header", "Body", eeRadioButtons \| eeIconStop \| eeHideStopMacro );

if( result != 0 ) alert( menu.GetText( result ) );

#### \[VBScript\]

Set menu = CreatePopupMenu()

menu.Add "Button 1", 1, eeMenuChecked

menu.Add "Button 2", 2

result = menu.MsgBox( "Header", "Body", eeIconInformation )

If result <> 0 Then alert( menu.GetText( result ) )

result = menu.MsgBox( "Header", "Body", eeCommandLinks Or eeIconExclamation )

If result <> 0 Then alert( menu.GetText( result ) )

result = menu.MsgBox( "Header", "Body", eeRadioButtons Or eeIconStop Or eeHideStopMacro )

If result <> 0 Then alert( menu.GetText( result ) )

## 版本

支持 EmEditor Professional v20.9 或之後的版本。
