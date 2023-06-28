# Editor\_Numbering

在鼠标位置或垂直选择处，插入编号。你能直接用该内联函数或明确地发送 [EE\_NUMBERING](../message/ee_numbering) 消息。

HRESULT Editor\_Numbering( HWND hwnd, LPCWSTR pszFirst, LPCWSTR pszInc, INT64 nMaxLines, UINT nFlags );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszFirst_

> 指定要在第一行插入的初始值或字符。

_pszInc_

> 指定十进制形式的增量。这是第一行和第二行之间的值的变化。

_nMaxLines_

> 指定十进制形式的行数。

_nFlags_

> 你可以指定以下值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | NUM\_FLAG\_CAPITAL\_LETTERS | 以大写字母插入十六进制值。 |
> | NUM\_FLAG\_SKIP\_EMPTY\_LINES | 在空行后继续编号，而不会在垂直选择模式或多选区模式期间对空行进行编号。 |
> | NUM\_FLAG\_RESTART\_NUM\_EMPTY | 在垂直选择模式或多选区模式下，编号在空行后将从第一个值重新开始。 |
> | NUM\_FLAG\_RESTART\_NUM\_DISCONTINUOUS | 在多选区模式下，编号将在不连续的行处从第一个值重新开始。 |
> | NUM\_FLAG\_DECIMAL | 以十进制形式插入数字。 |
> | NUM\_FLAG\_HEXADECIMAL | 以十六进制形式插入数字。 |
> | NUM\_FLAG\_OCTAL | 以八进制形式插入数字。 |
> | NUM\_FLAG\_BINARY | 以二进制形式插入数字。 |
> | NUM\_FLAG\_OTHER | 插入字符而不是数字。从 _pszFirst_ 参数中指定的数字开始，此选项插入用在 _pszInc_ 参数中指定的 Unicode 值的增量的连续字符。每行只能插入一个字符。 |

## 返回值

> 如果成功的话，返回值为 0。

## 版本

> 支持 EmEditor Professional 19.1 或之后的版本。