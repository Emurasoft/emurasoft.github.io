# EP\_SYNC\_NOW

如果支持同步功能，則指示外掛程式立即同步。

EP\_SYNC\_NOW

hwnd = hwndView;

wParam = nFlags;

lParam = 0;

## 參數

_hwndView_

> EmEditor 視圖的視窗控點。如果無法確定活動視圖，則此值可以為 NULL。

_nFlags_

> 此標志可以包括以下值的組合。SYNC\_SETTINGS\_SEND 和 SYNC\_SETTINGS\_RECEIVE 不能同時指定。
>
> | 值 | 含義 |
> | --- | --- |
> | SYNC\_SETTINGS\_SEND | 外掛程式應發送設定。 |
> | SYNC\_SETTINGS\_RECEIVE | 外掛程式應接收設定。 |
> | SYNC\_FLAG\_FORCE | 即使設定檔案的時間戳記很舊，外掛程式也應該接收設定。 |
> | SYNC\_FLAG\_REFRESH\_UI | 外掛程式應在收到設定後更新 UI。 |

## 返回值

> 返回值被忽略。

## 版本

> 支持 Version 20.9 或之後的版本。