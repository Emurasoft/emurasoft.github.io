# Editor\_SetStatusW

ステータスメッセージにUnicode文字列を設定します。このインライン関数を使うか、または
[EE\_SET\_STATUSW メッセージ](../message/ee_set_statusw) を直接送ることができます。

Editor\_SetStatusW( HWND hwnd, LPCWSTR szStatus, UINT nFlags = 0 );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szStatus_

> ステータスバーに表示するメッセージ文字列を指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> | Value | Meaning |
> | --- | --- |
> | STATUS\_FLAG\_NONE | メッセージを通常の色で表示します。 |
> | STATUS\_FLAG\_MESSAGE | メッセージを既定の強調色で表示します。 |
> | STATUS\_FLAG\_WARNING | メッセージを黄色で表示します。 |
> | STATUS\_FLAG\_ERROR | メッセージを赤色で表示します。 |
> | STATUS\_FLAG\_ERASE\_SHORTLY | メッセージを数秒間表示して消去します。 |

## 戻り値

> 戻り値は利用されません。