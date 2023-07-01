# Editor\_GetUnicodeName

檢索指定字元或字串的 Unicode 名。你能直接用該內嵌函式或明確地發送 [EE\_GET\_UNICODE\_NAME](../message/ee_get_unicode_name) 消息。

int Editor\_GetUnicodeName( HWND hwnd, LPWSTR pBuf, int cchBuf, LPCWSTR pstrSrc, int cchSrc );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pBuf_

> 指定指針指向的能檢索 Unicode 名的緩衝區。

_cchBuf_

> 以字節為單位指定緩衝區大小，包括終止空字元。

_pstrSrc_

> 指定源字元或字串。

_cchSrc_

> 指定在 _pstrSrc_ 中指定的字元數。

## 返回值

> 如果 UNICODE\_NAME\_INFO 結構的 _cchBuf_ 欄位是零，那返回值則是用字元數表示的一個會接收文字的緩衝區的必需大小。

## 版本

> 支持 EmEditor Professional 19.1 或之後的版本。
