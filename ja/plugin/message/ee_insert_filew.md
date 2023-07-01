# EE\_INSERT\_FILEW

指定するファイルの中身をカーソル位置に挿入します。ファイル名は、Unicode文字列で指定します。このメッセージを直接送るか、または
[Editor\_InsertFileW インライン関数](../macro/editor_insertfilew) を使うことができます。

EE\_INSERT\_FILEW

wParam = (WPARAM) (LOAD\_FILE\_INFO\_EX\*) pLoadFileInfoEx;

lParam = (LPARAM) (LPCWSTR) szFileName;

## パラメータ

_pLoadFileInfoEx_

> [LOAD\_FILE\_INFO\_EX 構造体](../structure/load_file_info) へのポインタを指定します。NULLを指定すると、プロパティで設定された既定値で開きます。

_szFileName_

> 読み込むファイル名をフルパスで指定します。存在しないファイル名を指定すると、エラーが発生します。

## 戻り値

> 成功すると 0 以外を返します。失敗すると 0 を返します。
