# EE\_MANAGE\_DUPLICATES

删除或把重复行设为书签。你可以明确地发送该消息或用 [Editor\_ManageDuplicates](../macro/editor_manageduplicates) 内联函数。

EE\_MANAGE\_DUPLICATES

wParam = 0;

lParam = (LPARAM) (MANAGE\_DUPLICATES\_INFO\*) pManageDuplicatesInfo;

## 参数

_pManageDuplicatesInfo_

> 指向 [MANAGE\_DUPLICATES\_INFO](../structure/manage_duplicates_info) 结构。

## 返回值

> 返回 HRESULT 值。0 或正值表示成功，负值表示失败。

## 版本

> 支持 EmEditor Professional Version 16.4 或之后的版本。
