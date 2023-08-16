# CUSTOM\_BAR\_INFO

[Editor\_CustomBarOpen インライン関数](../macro/editor_custombaropen) ( [EE\_CUSTOM\_BAR\_OPEN メッセージ](../message/ee_custom_bar_open)) で使用します。

```
typedef struct _CUSTOM_BAR_INFO {
	size_t cbSize;
	HWND hwndCustomBar;
	HWND hwndClient;
	LPCTSTR pszTitle;
	int iPos;
} CUSTOM_BAR_INFO;
```

## フィールド

_cbSize_

\[入力\] sizeof( CUSTOM\_BAR\_INFO ) を指定します。

_hwndCustomBar_

\[出力\] 成功すると、カスタム バー ウィンドウへのハンドルが格納されます。

_hwndClient_

\[入力\] クライアント ウィンドウへのハンドルを指定します。

_pszTitle_

\[入力\] カスタム バーのタイトル文字列を指定します。

_iPos_

\[入力\] カスタム バーの初期状態の位置を下記の中から選択して指定します。

|     |     |
| --- | --- |
| 値 | 意味 |
| 0 | ウィンドウの左側 |
| 1 | ウィンドウの上部 |
| 2 | ウィンドウの右側 |
| 3 | ウィンドウの下部 |

## バージョン

Version 6.00 以上で利用できます。
