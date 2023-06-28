# EP\_GET\_BITMAP

ツールバーに表示される様々なサイズと色数のプラグイン ボタンのビットマップのリソースIDを取得します。

EP\_GET\_BITMAP

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## パラメータ

_hwndParent_

> EmEditor のフレームのウィンドウ ハンドルが格納されています。

_flags_

> 取得するツールバー ボタンのサイズと色数と状態を指定します。次の値の組み合わせになります。
>
> | 定数 | 説明 |
> | --- | --- |
> | BITMAP\_SMALL | 小さいサイズのビットマップ (16x16ピクセル) |
> | BITMAP\_LARGE | 大きいサイズのビットマップ (24x24ピクセル) |
> | BITMAP\_16\_COLOR | 16色のビットマップ |
> | BITMAP\_24BIT\_COLOR | 24bit色(True Color)のビットマップ |
> | BITMAP\_256\_COLOR | 256色のビットマップ |
> | BITMAP\_DEFAULT | 通常状態のビットマップ |
> | BITMAP\_DISABLED | 無効状態のビットマップ |
> | BITMAP\_HOT | 強調状態のビットマップ |

## 戻り値

> 要求されたサイズと色数のビットマップリソースIDを返さなければなりません。0を返すと、EmEditor は、エクスポートする関数
> GetBitmapID を使って、小さいサイズ、16色ビットマップのリソースIDを取得します。