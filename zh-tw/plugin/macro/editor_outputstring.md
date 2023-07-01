# Editor\_OutputString

追加一個字串到輸出列中。您能直接用該內嵌函式或明確地發送 [EE\_OUTPUT\_STRING](../message/ee_output_string) 消息。

Editor\_OutputString( HWND hwnd, LPCWSTR szString, UINT nFlags );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szString_

> 指定要被追加的字串。

_nFlags_

> 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | FLAG\_OPEN\_OUTPUT | 打開輸出列。 |
> | FLAG\_CLOSE\_OUTPUT | 關閉輸出列。 |
> | FLAG\_FOCUS\_OUTPUT | 把鍵盤焦點設置到輸出列上。 |
> | FLAG\_CLEAR\_OUTPUT | 清除輸出列中的內容。 |

## 返回值

> 如果消息成功，返回值為非零值。如果消息不成功，返回值為零。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
