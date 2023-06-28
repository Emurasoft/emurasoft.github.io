# Editor\_LoadFileA

文書を指定するファイルから読みこんで表示します。ファイル名は、ANSI文字列で指定します。このインライン関数を使うか、または
[EE\_LOAD\_FILEA メッセージ](../message/ee_load_filea) を直接送ることができます。

Editor\_LoadFileA( HWND hwnd, LOAD\_FILE\_INFO\_EX\* pLoadFileInfo, LPCSTR szFileName
);

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pLoadFileInfo_

> [LOAD\_FILE\_INFO\_EX 構造体](../structure/load_file_info) へのポインタを指定します。NULLを指定すると、プロパティで設定された既定値で開きます。

_szFileName_

> 読み込むファイル名をフルパスで指定します。存在しないファイル名を指定すると、エラーが発生します。

## 戻り値

> 成功すると 0 以外を返します。失敗すると 0 を返します。