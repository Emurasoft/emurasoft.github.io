# Editor\_GetLineA

在指定行檢索 ANSI 文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_LINEA](../message/ee_get_linea) 消息。

Editor\_GetLineA( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPSTR szString );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pGetLineInfo_

指標至 [GET\_LINE\_INFO](../structure/get_line_info) 結構。

_szString_

指標至會接收文字的緩沖區。

## 返回值

如果 _pGetLineInfo->cch_  為零，必須要有以位元為單位的返回值來表示接收文字的緩沖區。如果 _pGetLineInfo->cch_ 非零，不使用返回值。
