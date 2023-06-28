# EE\_OUTPUT\_STRING

追加一个字符串到输出栏中。你能明确地发送该消息或用 [Editor\_OutputString](../macro/editor_outputstring) 内联函数。

EE\_OUTPUT\_STRING

wParam = nFlags;

lParam = (LPARAM) (LPCWSTR) szString;

## 参数

_nFlags_

> 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_OPEN\_OUTPUT | 打开输出栏。 |
> | FLAG\_CLOSE\_OUTPUT | 关闭输出栏。 |
> | FLAG\_FOCUS\_OUTPUT | 把键盘焦点设置到输出栏上。 |
> | FLAG\_CLEAR\_OUTPUT | 清除输出栏中的内容。 |

_szString_

> 指定要被追加的字符串。

## 返回值

> 如果消息成功，返回值为非零值。如果消息不成功，返回值为零。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。