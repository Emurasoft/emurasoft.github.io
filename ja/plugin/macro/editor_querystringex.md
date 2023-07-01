# Editor\_QueryStringEx

指定するコマンドに関連する文字列を取得します。このメッセージは MAX\_PATH 文字を超える長いファイル パスをサポートしています。このインライン関数を使うか、または
[EE\_QUERY\_STRING\_EX メッセージ](../message/ee_query_string_ex) を直接送ることができます。

Editor\_QueryString( HWND hwnd, UINT nCmdID, LPWSTR pBuf, UINT cchBuf, UINT nFlags );

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

_pBuf_

> 文字列を取得するバッファを指定します。

_cchBuf_

> バッファのサイズを文字数で指定します。

_nFlags_

> 次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | QUERY\_STRING\_LONG\_TITLE | 長いバージョンの文字列が必要なことを示します。 |
> | QUERY\_STRING\_SHORT\_TITLE | 短いバージョンの文字列が必要なことを示します。 |

## 戻り値

> 成功すると S\_OK を返します。それ以外の場合は負の値を返します。

## バージョン

EmEditor Professional Version 20.6 以上で利用できます。
