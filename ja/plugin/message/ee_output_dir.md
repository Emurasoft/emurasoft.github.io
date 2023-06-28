# EE\_OUTPUT\_DIR

アウトプット バーにカレント ディレクトリを設定します。このメッセージを直接送るか、または
[Editor\_OutputDir インライン関数](../macro/editor_outputdir) を使うことができます。

EE\_OUTPUT\_DIR

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szCurrDir;

## パラメータ

_szCurrDir_

> カレント ディレクトリを指定します。この情報は、テキストがカレント ディレクトリからしかジャンプできない相対パスを含む場合に必要です。

## 戻り値

> 戻り値は利用されません。

## バージョン

> EmEditor Version 7.00 以上で利用できます。