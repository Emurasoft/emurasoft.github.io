# EE\_INSERT\_FILEA

指定するファイルの中身をカーソル位置に挿入または上書きします。ファイル名は、ANSI文字列で指定します。このメッセージを直接送るか、または
[Editor\_InsertFileA インライン関数](../macro/editor_insertfilea) を使うことができます。

```
EE_INSERT_FILEA
wParam = (WPARAM) (LOAD_FILE_INFO_EX*) pLoadFileInfoEx;
lParam = (LPARAM) (LPCSTR) szFileName;
```

## パラメータ

_pLoadFileInfo_

[LOAD\_FILE\_INFO\_EX 構造体](../structure/load_file_info) へのポインタを指定します。NULLを指定すると、プロパティで設定された既定値で開きます。

_szFileName_

読み込むファイル名をフルパスで指定します。存在しないファイル名を指定すると、エラーが発生します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。
