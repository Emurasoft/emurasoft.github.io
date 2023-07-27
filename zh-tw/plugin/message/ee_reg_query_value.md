# EE\_REG\_QUERY\_VALUE

根據 EmEditor 的設定，從注冊表或一個 INI 檔案中檢索數據的特定值。您能明確地發送該消息或用 [Editor\_RegQueryValue](../macro/editor_regqueryvalue) 內嵌函式。

EE\_REG\_QUERY\_VALUE

wParam = 0;

(REG\_QUERY\_VALUE\_INFO\*)lParam = pRegQueryValueInfo;

## 參數

_pRegSetValueInfo_

指針指向 [REG\_QUERY\_VALUE\_INFO 結構](../structure/reg_query_value_info)。

## 返回值

如果消息成功，返回值是 ERROR\_SUCCESS。

如果消息不成功，返回值是一個在 Winerror.h 中被定義的非零的錯誤代碼。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
