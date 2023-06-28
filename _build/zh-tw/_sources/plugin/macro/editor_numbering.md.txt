# Editor\_Numbering

在游標位置或垂直選擇處，插入編號。你能直接用該內嵌函式或明確地發送 [EE\_NUMBERING](../message/ee_numbering) 消息。

HRESULT Editor\_Numbering( HWND hwnd, LPCWSTR pszFirst, LPCWSTR pszInc, INT64 nMaxLines, UINT nFlags );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pszFirst_

> 指定要在第一行插入的初始值或字元。

_pszInc_

> 指定十進位形式的增量。這是第一行和第二行之間的值的變化。

_nMaxLines_

> 指定十進位形式的行數。

_nFlags_

> 你可以指定以下值的組合。
>
> | 值 | 含義 |
> | --- | --- |
> | NUM\_FLAG\_CAPITAL\_LETTERS | 以大寫字母插入十六進位值。 |
> | NUM\_FLAG\_SKIP\_EMPTY\_LINES | 在空行后繼續編號，而不會在垂直選擇模式或多選區模式期間對空行進行編號。 |
> | NUM\_FLAG\_RESTART\_NUM\_EMPTY | 在垂直選擇模式或多選區模式下，編號在空行后將從第一個值重新開始。 |
> | NUM\_FLAG\_RESTART\_NUM\_DISCONTINUOUS | 在多選區模式下，編號將在不連續的行處從第一個值重新開始。 |
> | NUM\_FLAG\_DECIMAL | 以十進位形式插入數字。 |
> | NUM\_FLAG\_HEXADECIMAL | 以十六進位形式插入數字。 |
> | NUM\_FLAG\_OCTAL | 以八進位形式插入數字。 |
> | NUM\_FLAG\_BINARY | 以二進位形式插入數字。 |
> | NUM\_FLAG\_OTHER | 插入字元而不是數字。從 _pszFirst_ 參數中指定的數字開始，此選項插入用在 _pszInc_ 參數中指定的 Unicode 值的增量的連續字元。每行只能插入一個字元。 |

## 返回值

> 如果成功的話，返回值為 0。

## 版本

> 支持 EmEditor Professional 19.1 或之後的版本。