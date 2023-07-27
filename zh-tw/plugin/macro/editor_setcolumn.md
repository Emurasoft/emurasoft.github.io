# Editor\_SetColumn

設置一列文字。你能用該內嵌函式或明確地發送
[EE\_SET\_COLUMN](../message/ee_set_column) 消息。

Editor\_SetColumn( HWND hwnd, SET\_COLUMN\_INFO\* pSetColumnInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pSetLineInfo_

指針指向 [COLUMN\_STRUCT](../structure/column_struct) 結構。

## 返回值

如果成功，返回值為零或正數值，如果失敗，返回負數值。
