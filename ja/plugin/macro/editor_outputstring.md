# Editor\_OutputString

アウトプット バーに文字列を追加します。このインライン関数を使うか、または
[EE\_OUTPUT\_STRINGメッセージ](../message/ee_output_string) を直接送ることができます。

Editor\_OutputString( HWND hwnd, LPCWSTR szString, UINT nFlags );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | FLAG\_OPEN\_OUTPUT | アウトプット バーを開きます。 |
> | FLAG\_CLOSE\_OUTPUT | アウトプット バーを閉じます。 |
> | FLAG\_FOCUS\_OUTPUT | アウトプット バーにキーボード フォーカスを設定します。 |
> | FLAG\_CLEAR\_OUTPUT | アウトプット バーの中身をクリアします。 |

_szString_

> 追加する文字列を指定します。

## 戻り値

> 成功すると 0 以外を返します。失敗すると 0 を返します。

## バージョン

> EmEditor Version 7.00 以上で利用できます。
