# Editor\_GetOutputString

檢索輸出列中的文字。您能直接用該內嵌函式或明確地發送 [EE\_GET\_OUTPUT\_STRING](../message/ee_get_output_string)
消息。

Editor\_GetOutputString( HWND hwnd, UINT cchBuf, LPWSTR pBuf );

## 參數

_cchBuf_

以位元為單位指定緩沖區大小，包括終止空字元。

_pBuf_

指定指標至接收文字的緩沖區。

## 返回值

返回值是用來接收文字的以位元為單位的緩沖區大小，包括終止空字元。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
