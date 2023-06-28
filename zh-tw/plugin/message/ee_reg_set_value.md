# EE\_REG\_SET\_VALUE

根據 EmEditor 的設定，設一個值到注冊表或一個 INI 檔案中。您能明確地發送該消息或用 [Editor\_RegSetValue](../macro/editor_regsetvalue) 內嵌函式。

EE\_REG\_SET\_VALUE

wParam = 0;

(REG\_SET\_VALUE\_INFO\*)lParam = pRegSetValueInfo;

## 參數

_pRegSetValueInfo_

> 指針指向 [REG\_SET\_VALUE\_INFO 結構](../structure/reg_set_value_info)。

## 返回值

> 如果消息成功，返回值是 ERROR\_SUCCESS。
>
> 如果消息不成功，返回值是一個在 Winerror.h 中被定義的非零的錯誤代碼。

## 支持版本

支持 EmEditor 7.00 或之後的版本。