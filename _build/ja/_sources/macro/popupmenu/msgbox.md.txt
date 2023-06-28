# MsgBox メソッド

オブジェクトにより提供された情報をもとにダイアログ ボックスを表示して、選択されたボタン、ラジオ ボタン、またはコマンド リンクの ID を返します。このメッセージはセパレータとサブ メニューを無視します。

#### \[JavaScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ );

#### \[VBScript\]

id = popupmenu. **MsgBox**( _message_, _message2_, _flags_ )

## パラメータ

_strMessage_

表示する文字列を指定します。

_strMessage2_

省略可能。最初のメッセージの下に表示する追加の文字列を指定します。

_flags_

省略可能。次の値の組み合わせを指定します。eeCommandLinks と eeRadioButtons は同時に指定することはできません。

|     |     |
| --- | --- |
| eeCommandLinks | メニュー項目がプッシュ ボタンの代わりにコマンド リンクとして表示されることを示します。 |
| eeRadioButtons | メニュー項目がプッシュ ボタンの代わりにラジオ ボタンとして表示されることを示します。 |
| eeHideStopMacro | ダイアログ ボックスから \[マクロの停止\] チェック ボックスを非表示にします。 |
| eeIconStop | ダイアログ ボックスに停止サインのアイコンを表示します。 |
| eeIconExclamation | ダイアログ ボックスに感嘆符のアイコンを表示します。 |
| eeIconInformation | ダイアログ ボックスに丸の中に小文字の i があるアイコンを表示します。 |

## 例

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

## バージョン

EmEditor Professional Version 20.9 以上で利用できます。