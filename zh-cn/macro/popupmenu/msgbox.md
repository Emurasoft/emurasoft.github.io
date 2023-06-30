# MsgBox 方法 (PopupMenu ����)

根据对象提供的信息显示对话框，并检索所选按钮、单选按钮或命令链接的标识符。此方法忽略分隔项和子菜单。

#### \[JavaScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ );

#### \[VBScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ )

## 参数

_strMessage_

指定要显示的消息。

_strMessage2_

可选。指定要在第一条消息下方显示的附加消息。

_flags_

可选。指定以下值的组合。eeCommandLinks 和 eeRadioButtons 不能合用。

|     |     |
| --- | --- |
| eeCommandLinks | 指示菜单项将显示为命令链接而不是按钮。 |
| eeRadioButtons | 指示菜单项将显示为单选按钮而不是按钮。 |
| eeHideStopMacro | 从对话框中隐藏停止宏复选框。 |
| eeIconStop | 对话框中出现一个停止标志图标。 |
| eeIconExclamation | 对话框中出现一个感叹号图标。 |
| eeIconInformation | 对话框中出现一个由圆圈中的小写字母 i 组成的图标。 |

## 示例

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

支持 EmEditor Professional v20.9 或之后的版本。