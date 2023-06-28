# Editor\_QueryString

指定するコマンドに関連する文字列を取得します。このインライン関数を使うか、または
[EE\_QUERY\_STRING メッセージ](../message/ee_query_string) を直接送ることができます。

Editor\_QueryString( HWND hwnd, UINT nCmdID, LPWSTR psz, BOOL bShortTitle = FALSE );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nCmdID_

> 実行したいコマンドを整数の ID で指定します。次のコマンドのみ使用することができます。詳しくは、 [コマンド \
> リファレンス](../../cmd/index) を参照してください。
>
> |     |     |     |
> | --- | --- | --- |
> | nID | コマンド名 | 戻り値 |
> | 4609 から 4609 + 63 まで | [最近使ったファイルの一覧](../../cmd/file/file_mru_file1) | ファイルのパスと名前 |
> | 4864 から 4864 + 63 まで | [最近使ったファイルの挿入用一覧](../../cmd/file/file_mru_insert1) | ファイルのパスと名前 |
> | 4992 から 4992 + 63 まで | [最近使ったフォルダの一覧](../../cmd/file/file_mru_folder1) | ファイルのパスと名前 |
> | 5376 から 5376 + 255 まで | [文書の一覧](../../cmd/window/window_menu) | ウィンドウ タイトル |
> | 5632 から 5632 + 255 まで | [プラグインの一覧](../../cmd/tools/plug_in1) | プラグインのファイル名 |
> | 6656 から 6656 + 255 まで | [読み直しエンコードの一覧](../../cmd/file/file_reload_defined) | エンコード名 |
> | 7680 から 7680 + 255 まで | [保存エンコードの一覧](../../cmd/file/file_save_defined) | エンコード名 |
> | 9216 から 9216 + 1023 まで | [マイ マクロの一覧](../../cmd/macros/macro1) | マクロのパスと名前 |

_bShortTitle_

> 特定のコマンドにおいて短いバージョンの文字列が必要かどうかを指定します。

_psz_

> 文字列を取得するバッファを指定します。

## 戻り値

> コマンド ID が正しければ 0 以外を返します。それ以外の場合 0 を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。