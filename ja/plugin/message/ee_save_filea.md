# EE\_SAVE\_FILEA

文書を指定するファイルに保存します。ファイル名は、ANSI文字列で指定します。このメッセージを直接送るか、 [Editor\_DocSaveFileA インライン関数](../macro/editor_docsavefilea)、または
[Editor\_SaveFileA インライン関数](../macro/editor_savefilea) を使うことができます。

EE\_SAVE\_FILEA

wParam = (WPARAM) MAKEWPARAM((bReplace), (iDoc)+1);

lParam = (LPARAM) (LPSTR) szFileName;

または

EE\_SAVE\_FILEA

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPSTR) szFileName;

## パラメータ

_bReplace_

名前をつけて保存する場合は TRUE を、コピーを保存する場合は FALSE を指定します。

_iDoc_

対象となる文書のインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブな文書を対象とします。

_szFileName_

保存するファイル名をフルパスで指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。

## バージョン

Version 3.00 以上で利用できます。ただし、iDoc パラメータは Version 5.00 以上で利用できます。
