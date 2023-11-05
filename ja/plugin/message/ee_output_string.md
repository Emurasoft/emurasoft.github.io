# EE\_OUTPUT\_STRING

アウトプット バーに文字列を追加します。このメッセージを直接送るか、または
[Editor\_OutputString インライン関数](../macro/editor_outputstring) を使うことができます。

```
EE_OUTPUT_STRING
wParam = nFlags;
lParam = (LPARAM) (LPCWSTR) szString;
```

## パラメータ

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| FLAG\_OPEN\_OUTPUT | アウトプット バーを開きます。 |
| FLAG\_CLOSE\_OUTPUT | アウトプット バーを閉じます。 |
| FLAG\_FOCUS\_OUTPUT | アウトプット バーにキーボード フォーカスを設定します。 |
| FLAG\_CLEAR\_OUTPUT | アウトプット バーの中身をクリアします。 |

_szString_

追加する文字列を指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。

## バージョン

EmEditor Version 7.00 以上で利用できます。
