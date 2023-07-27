# EE\_MANAGE\_DUPLICATES

刪除或把重複行設為書籤。你可以明確地發送該消息或用 [Editor\_ManageDuplicates](../macro/editor_manageduplicates) 內嵌函式。

EE\_MANAGE\_DUPLICATES

wParam = 0;

lParam = (LPARAM) (MANAGE\_DUPLICATES\_INFO\*) pManageDuplicatesInfo;

## 參數

_pManageDuplicatesInfo_

指向 [MANAGE\_DUPLICATES\_INFO](../structure/manage_duplicates_info) 結構。

## 返回值

返回 HRESULT 值。0 或正值表示成功，負值表示失敗。

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。
