# EE\_OUTPUT\_STRING

追加一個字符串到輸出列中。您能明確地發送該消息或用 [Editor\_OutputString](../macro/editor_outputstring) 內嵌函式。

```
EE_OUTPUT_STRING
wParam = nFlags;
lParam = (LPARAM) (LPCWSTR) szString;
```

## 參數

_nFlags_

從如下值中指定一個組合。

|     |     |
| --- | --- |
| FLAG\_OPEN\_OUTPUT | 打開輸出列。 |
| FLAG\_CLOSE\_OUTPUT | 關閉輸出列。 |
| FLAG\_FOCUS\_OUTPUT | 把鍵盤焦點設置到輸出列上。 |
| FLAG\_CLEAR\_OUTPUT | 清除輸出列中的內容。 |

_szString_

指定要被追加的字符串。

## 返回值

如果消息成功，返回值為非零值。如果消息不成功，返回值為零。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
