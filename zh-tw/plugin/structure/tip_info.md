# TIP\_INFO

用於 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息。

typedef struct \_TIP\_INFO {

UINT cbSize;

LPCWSTR pszTip;

POINT\_PTR ptCaret;

POINT ptDev;

UINT nFlags;

} TIP\_INFO;

## 成員

_cbSize_

以字節為單位的數據結構大小。在發送 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息之前，把這個成員設為sizeof ( TIP\_INFO )。

_pszTip_

指定在工具提示中顯示的文字。文字長度不能超過 3,999 個字元。該字串可包含以這種格式指定的可點擊文字："<a href="url">可點擊文字</a>"。

_ptCaret_

目前不使用。

_ptDev_

目前不使用。

_nFlags_

指定一個下列值的組合。

|     |     |
| --- | --- |
| SHOW\_TIP\_ACTIVE\_STRING | 在游標懸停的主動字串處顯示工具提示。 |
| SHOW\_TIP\_CURRENT\_CARET | 在插入符號位置顯示工具提示。 |
| SHOW\_TIP\_CURRENT\_MOUSE | 在游標指針位置顯示工具提示。 |
| SHOW\_TIP\_HIDE | 如果已經顯示，隱藏工具提示。 |

## 版本

支持 EmEditor Professional 16.9 或之後的版本。
