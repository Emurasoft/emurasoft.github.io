# Editor\_GetPageSize

檢索頁面大小。您能直接用該內嵌函式或明確地發送
[EE\_GET\_PAGE\_SIZE](../message/ee_get_page_size)
消息。

Editor\_GetPageSize( HWND hwnd, SIZE\_PTR\* psizePage );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_psizePage_

> 指標至一個會接收頁面大小的 [SIZE\_PTR 結構](../structure/size_ptr)。頁面大小是一組由在目前的 EmEditor 視窗大小中可以顯示的行數以及列數構成的數字。

## 返回值

> 不使用返回值。
