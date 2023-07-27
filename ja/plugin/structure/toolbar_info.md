# TOOLBAR\_INFO

[Editor\_ToolbarOpen インライン関数](../macro/editor_toolbaropen) （ [EE\_TOOLBAR\_OPEN メッセージ](../message/ee_toolbar_open)） とカスタム ツール バーに関連したイベントで使用します。

typedef struct \_TOOLBAR\_INFO {

size\_t cbSize;

HWND hwndRebar;

HWND hwndClient;

LPCTSTR pszTitle;

UINT nMask;

UINT nID;

UINT nFlags;

UINT fStyle;

UINT cxMinChild;

UINT cyMinChild;

UINT cx;

UINT cxIdeal;

UINT nBand;

WORD wPlugInCmdID;

} TOOLBAR\_INFO;

## フィールド

_cbSize_

このデータ構造体のサイズをバイト数で指定します。TOOLBAR\_INFO メッセージを送信する前に、このフィールドに sizeof(TOOLBAR\_INFO） を設定します。

_hwndRebar_

EmEditor は、ツール バーが EE\_TOOLBAR\_OPEN メッセージ ハンドラ内で作成されたとき、リバー ウィンドウへのハンドルを保存します。

_hwndClient_

クライアントのツール バー ウィンドウへのハンドルを指定します。

_pszTitle_

ツール バーのタイトル文字列を指定します。

_nMask_

以下の値の組み合わせを指定します。

|     |     |
| --- | --- |
| TIM\_REBAR | hwndRebar パラメータは有効です。 |
| TIM\_CLIENT | hwndClient パラメータは有効です。 |
| TIM\_TITLE | pszTitle パラメータは有効です。 |
| TIM\_ID | nID パラメータは有効です。 |
| TIM\_FLAGS | nFlags パラメータは有効です。 |
| TIM\_STYLE | fStyle パラメータは有効です。 |
| TIM\_MINCHILD | cxMinChild と cyMinChild パラメータは有効です。 |
| TIM\_CX | cx パラメータは有効です。 |
| TIM\_CXIDEAL | cxIdeal パラメータは有効です。 |
| TIM\_BAND | nBand パラメータは有効です。 |
| TIM\_PLUG\_IN\_CMD\_ID | wPlugInCmdID パラメータは有効です。 |

_nID_

ツールバーの ID を指定します。

_nFlags_

ツールバーが閉じた原因を指定します。

|     |     |
| --- | --- |
| 0 | ユーザーによって閉じられます。 |
| CLOSED\_FRAME\_WINDOW | フレーム ウィンドウが閉じられます。 |

_fStyle_

バンドのスタイルを指定するフラグです。ツール バーを非表示にするには RBBS\_HIDDEN を含めます。このパラメータは REBARBANDINFO 構造体の fStyle パラメータと同一です。

_cxMinChild_

子ウィンドウの最小幅をピクセル単位で指定します。このパラメータは REBARBANDINFO 構造体の cxMinChild パラメータと同一です。

_cyMinChild_

子ウィンドウの最小の高さをピクセル単位で指定します。このパラメータは REBARBANDINFO 構造体の cyMinChild パラメータと同一です。

_cx_

バンドの長さをピクセル単位で指定します。このパラメータは REBARBANDINFO 構造体の cx パラメータと同一です。

_cxIdeal_

バンドの幅をピクセル単位で指定します。このパラメータは REBARBANDINFO 構造体の cxIdeal パラメータと同一です。

_nBand_

バンドを挿入する位置の 0 から始まる、インデックスを指定します。このパラメータに -1 を指定すると、リバー コントロールは最後の位置に新しいバンドを追加します。

_wPlugInCmdID_

プラグインのコマンド ID を指定します。

## バージョン

Version 7.00 以上で利用できます。
