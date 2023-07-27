# EE\_SET\_STATUSW

ステータスメッセージにUnicode文字列を設定します。このメッセージを直接送るか、または [Editor\_SetStatusW \
インライン関数](../macro/editor_setstatusw) を使うことができます。

EE\_SET\_STATUSW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szStatus;

## パラメータ

_szStatus_

ステータスバーに表示するメッセージ文字列を指定します。

_nFlags_

次の値の組み合わせを指定します。

| Value | Meaning |
| --- | --- |
| STATUS\_FLAG\_NONE | メッセージを通常の色で表示します。 |
| STATUS\_FLAG\_MESSAGE | メッセージを既定の強調色で表示します。 |
| STATUS\_FLAG\_WARNING | メッセージを黄色で表示します。 |
| STATUS\_FLAG\_ERROR | メッセージを赤色で表示します。 |
| STATUS\_FLAG\_ERASE\_SHORTLY | メッセージを数秒間表示して消去します。 |

## 戻り値

戻り値は利用されません。
