# Editor\_OutputDir

アウトプット バーにカレント ディレクトリを設定します。このインライン関数を使うか、または
[EE\_OUTPUT\_DIRメッセージ](../message/ee_output_dir) を直接送ることができます。

Editor\_OutputDir( HWND hwnd, LPCWSTR szCurrDir );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szCurrDir_

> カレント ディレクトリを指定します。この情報は、テキストがカレント ディレクトリからしかジャンプできない相対パスを含む場合に必要です。

## 戻り値

> 戻り値は利用されません。

## バージョン

> EmEditor Version 7.00 以上で利用できます。
