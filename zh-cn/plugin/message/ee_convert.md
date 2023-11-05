# EE\_CONVERT

转换字符。你能明确地发送该消息或用
[Editor\_Convert](../macro/editor_convert) 内联函数。

```
EE_CONVERT
wParam = (WPARAM) (UINT) nFlags;
lParam = (LPARAM) (LPCWSTR) szChars;
```

## 参数

_nFlags_

你能指定下列数值的组合。

| 值 | 含义 |
| --- | --- |
| FLAG\_MAKE\_LOWER | 转换为小写字符。 |
| FLAG\_MAKE\_UPPER | 转换为大写字符。 |
| FLAG\_HAN\_TO\_ZEN | 转换为全角字符。 |
| FLAG\_ZEN\_TO\_HAN. | 转换为半角字符。 |
| FLAG\_CAPITALIZE | 每一个单词的首字母大写。 |
| FLAG\_MAKE\_LOWER\_L | 转换为小写字符（与区域设置相关）。 |
| FLAG\_MAKE\_UPPER\_L | 转换为大写字符（与区域设置相关）。 |
| FLAG\_CAPITALIZE\_L | 将每个单词的首字母大写（与区域设置相关）。 |
| FLAG\_CONVERT\_SELECT\_ALL | 转换整个文本。如果没有设置该标志，EE\_CONVERT 仅转换选区内的字符。 |
| FLAG\_CONVERT\_KATA | 转换片假名。 |
| FLAG\_CONVERT\_ALPHANUMERIC | 转换字母和数字字符。 |
| FLAG\_CONVERT\_MARK | 转换标记。 |
| FLAG\_CONVERT\_SPACE | 转换空格。 |
| FLAG\_CONVERT\_KANA\_MARK | 转换假名标记。 |
| FLAG\_CONVERT\_CUSTOM | 当指定 FLAG\_HAN\_TO\_ZEN 或 FLAG\_ZEN\_TO\_HAN 时，szChars 参数指定应转换哪些单个字符。如果指定了此值，则还必须指定 szChars 参数，并忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
| FLAG\_JAPANESE\_YEN | 将 U+005C（反斜线号）转换为 U+FFE5（全角日元标记），反之亦然。 |
| FLAG\_KOREAN\_WON | 将 U+005C（反斜线号）转换为 U+FFE6（全角韩元标记），反之亦然。 |
| FLAG\_RIGHT\_SINGLE\_QUOTATION | 将 U+0027（撇号）转换为 U+2019（右单引号），反之亦然。 |
| FLAG\_RIGHT\_DOUBLE\_QUOTATION | 将 U+0022（引号）转换为 U+201D（右双引号），反之亦然。 |

_szChars_

如果指定了 FLAG\_CONVERT\_CUSTOM，则可以设置要转换的单个全角字符的组合。 如果不使用，请将此参数设置为 NULL。

## 返回值

如果消息成功，返回值为非零值。如果该消息不成功，返回值为零。
