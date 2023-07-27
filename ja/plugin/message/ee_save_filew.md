# EE\_SAVE\_FILEW

文書を指定するファイルに保存します。ファイル名は、Unicode文字列で指定します。このメッセージを直接送るか、 [Editor\_DocSaveFileW インライン関数](../macro/editor_docsavefilew)、または
[Editor\_SaveFileW インライン関数](../macro/editor_savefilew) を使うことができます。

EE\_SAVE\_FILEW

wParam = (WPARAM) MAKEWPARAM((bReplace), (iDoc)+1);

lParam = (LPARAM) (LPWSTR) szFileName;

または

EE\_SAVE\_FILEW

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPWSTR) szFileName;

## パラメータ

_bReplace_

名前をつけて保存する場合は TRUE を、コピーを保存する場合は FALSE を指定します。

_szFileName_

保存するファイル名をフルパスで指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。
