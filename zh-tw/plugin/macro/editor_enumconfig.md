# Editor\_EnumConfig

列舉可用的組態。您能直接用該內嵌函式或明確地發送 [EE\_ENUM\_CONFIG](../message/ee_enum_config) 消息。

Editor\_EnumConfig( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_cchBuf_

用字元數指定緩沖區大小。要注意的是兩個空字元會被添加到組態清單末尾。如果指定的數值為 0，該消息會返回檢索組態清單的必需大小。

_pBuf_

指定指標至緩沖區來檢索組態清單。在這個緩沖區內，由一個空字元分隔的可用的組態清單會被檢索。兩個空字元會被添加到組態清單末尾。如果指定的數值為 0，pBuf 是空 (NULL)。

## 返回值

返回值是檢索組態清單的必需大小。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
