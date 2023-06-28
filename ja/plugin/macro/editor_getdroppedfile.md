# Editor\_GetDroppedFile

最近ドロップされたファイルを取得します。このインライン関数を使うか、または

[EE\_GET\_DROPPED\_FILE メッセージ](../message/ee_get_dropped_file) を直接送ることができます。

Editor\_GetDroppedFile( HWND _hwnd_, int _nIndex_, LPWSTR
_pszBuf_ );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nIndex_

> ドロップされたファイルのインデックスを指定します。0 を基底とするインデックスを指定します。-1 を指定すると、ドロップされたファイルの数を取得します。

_pszBuf_

> ドロップされたファイル名を取得するバッファを指定します。バッファ サイズは、MAX\_PATH の文字数である必要があります。nIndex に -1
> を指定した場合、このパラメータには NULL を指定することができます。

## 戻り値

> 指定したインデックスのドロップされたファイルが存在する場合は 0 以外の値を返します。nIndex に -1
> を指定すると、ドロップされたファイルの数を取得します。

## バージョン

EmEditor Version 8.00 以上で利用できます。