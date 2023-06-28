# EE\_GET\_DROPPED\_FILE

最近ドロップされたファイルを取得します。このメッセージを直接送るか、 [Editor\_GetDroppedFile インライン関数](../macro/editor_getdroppedfile) を使うことができます。

EE\_GET\_DROPPED\_FILE

wParam = (WPARAM) (int) nIndex;

lParam = (LPARAM) (LPWSTR) pszBuf;

## パラメータ

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