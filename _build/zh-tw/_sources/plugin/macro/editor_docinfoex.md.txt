# Editor\_DocInfoEx

檢索或設定用於 EmEditor 的信息參數之一的值。你能直接用該內嵌函式或明確地發送
[EE\_INFO\_EX 消息](../message/ee_info_ex)。

Editor\_DocInfoEx( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## 參數

_nCmd_

> 指定要檢索或設定的參數。命令條目請參考 [EE\_INFO](../message/ee_info) 消息。

_hDoc_

> 指定目標文件的控點。如果指定 NULL，則目前使用中的文件將成為目標。根據 nCmd，也有可能不使用此參數。

_lParam_

> 取決於指定的參數。

## 返回值

> 取決於指定的參數。

## 支持版本

> 支持 EmEditor Professional v21.8 或之後的版本。