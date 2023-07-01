# Add 方法 (PopupMenu ��H)

添加一個新的項目到功能表末尾。

#### \[JavaScript\]

popupmenu. **Add**( _strText_, _id_, _flags_ );

#### \[VBScript\]

popupmenu. **Add** _strText_, _id_, _flags_

## 參數

_strText_

指定要顯示的文字。如果 eeMenuSeparator 在 _flags_ 參數中被設置，必須指定一個空字串。

_id_

指定新功能表項目的識別項。Track 方法把識別項作為返回值。如果 eeMenuSeparator 在 _flags_ 參數中被設置，必須指定 0。

_flags_

指定項目的狀態。能指定下列標志。

|     |     |
| --- | --- |
| eeMenuChecked | 把一個選中標記放在功能表項目旁。在功能表項旁邊放置一個核取標記。 |
| eeMenuGrayed | 停用功能表項目並且讓它變為灰色，這樣就不能選擇它。 |
| eeMenuSeparator | 畫一條水平分隔線。這個標志不能與其他標志合用。 |

## 版本

支持 EmEditor 5.00 或之後的版本。
