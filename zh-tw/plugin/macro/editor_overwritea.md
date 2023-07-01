# Editor\_OverwriteA

把一個 ANSI 字串插入到目前的游標位置處。這會覆寫已存在的字串。您能直接用該內嵌函式或明確地發送
[EE\_INSERT\_STRINGA](../message/ee_insert_stringa)
消息。

Editor\_OverwriteA( HWND hwnd, LPCSTR szString, bool bKeepDestReturnType = false );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szString_

> 指定要插入的字串。

_bKeepDestReturnType_

> 指定保持目標換行方式 (僅　CR，僅　LF，或　CR 和 LF) 。當該參數被省略時，EmEditor　會保持在　szString 參數中指定的換行方式。

## 返回值

> 不使用返回值。

## 支持版本

> bKeepDestReturnType 標志支持 EmEditor 7.00 或之後的版本。
