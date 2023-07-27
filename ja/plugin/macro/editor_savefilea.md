# Editor\_SaveFileA

現在アクティブな文書を指定するファイルに保存します。ファイル名は、ANSI文字列で指定します。このインライン関数を使うか、または
[EE\_SAVE\_FILEA メッセージ](../message/ee_save_filea) を直接送ることができます。

Editor\_SaveFileA( HWND hwnd, BOOL bReplace, LPSTR szFileName );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bReplace_

名前をつけて保存する場合は TRUE を、コピーを保存する場合は FALSE を指定します。

_szFileName_

保存するファイル名をフルパスで指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。

## バージョン

Version 3.00 以上で利用できます。
