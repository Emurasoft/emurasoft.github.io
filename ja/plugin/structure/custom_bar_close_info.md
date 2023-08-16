# CUSTOM\_BAR\_CLOSE\_INFO

[EVENT\_CUSTOM\_BAR\_CLOSED イベント](../event/index) で使用します。

typedef struct \_CUSTOM\_BAR\_CLOSE\_INFO {

UINT nID;

int iPos;

DWORD dwFlags;

} CUSTOM\_BAR\_CLOSE\_INFO;

## フィールド

_nID_

カスタム バー ID が格納されます。

_iPos_

閉じられる直前のカスタム バーの位置が格納されます。値は、下記の中のいずれかになります。

|     |     |
| --- | --- |
| 値 | 意味 |
| 0 | ウィンドウの左側 |
| 1 | ウィンドウの上部 |
| 2 | ウィンドウの右側 |
| 3 | ウィンドウの下部 |

_dwFlags_

カスタム バーが閉じられた原因が格納されます。値は、下記の中のいずれかになります。

|     |     |
| --- | --- |
| 値 | 意味 |
| 0 | ユーザーによって閉じられたことを示します。 |
| CLOSED\_FRAME\_WINDOW | フレーム ウィンドウが閉じられようとしていることを示します。 |
| CLOSED\_ANOTHER\_CUSTOM\_BAR | 他のカスタム バーが開かれたために、このカスタム バーが閉じられることを示します。 |

## バージョン

Version 6.00 以上で利用できます。
