# Editor\_InsertStringA

把一个 ANSI 字符串插入到当前光标位置处。取决于当前属性，这可能会改写已存在的字符串。你能直接用该内联函数或明确地发送 [EE\_INSERT\_STRINGA](../message/ee_insert_stringa) 消息。

Editor\_InsertStringA( HWND hwnd, LPCSTR szString, bool bKeepDestReturnType = false );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_szString_

> 指定要插入的字符串。

_bKeepDestReturnType_

> 指定保持目标换行方式（仅　CR，仅　ＬＦ　或 CR 以及　LF）。当该参数被省略时，EmEditor 会保持在 szString 参数中指定的换行方式。

## 返回值

> 不使用返回值。