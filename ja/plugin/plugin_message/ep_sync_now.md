# EP\_SYNC\_NOW

同期機能がサポートされていれば、プラグインへ今すぐ同期するように指示します。

EP\_SYNC\_NOW

hwnd = hwndView;

wParam = nFlags;

lParam = 0;

## パラメータ

_hwndView_

> EmEditor ビューのウィンドウ ハンドルが格納されています。この値は、アクティブなビューが決定できない場合には、0 になる可能性があります。

_nFlags_

> このフラグには、次の値の組み合わせが含まれます。SYNC\_SETTINGS\_SEND と SYNC\_SETTINGS\_RECEIVE の両方が含まれることはありません。
>
> | 値 | 意味 |
> | --- | --- |
> | SYNC\_SETTINGS\_SEND | プラグインは設定を送信します。 |
> | SYNC\_SETTINGS\_RECEIVE | プラグインは設定を受信します。 |
> | SYNC\_FLAG\_FORCE | プラグインは設定ファイルのタイム スタンプが古くても設定を受信します。 |
> | SYNC\_FLAG\_REFRESH\_UI | プラグインは設定を受信した後、UI を更新します。 |

## 戻り値

> 戻り値は無視されます。

## バージョン

> Version 20.9 以上で利用できます。
