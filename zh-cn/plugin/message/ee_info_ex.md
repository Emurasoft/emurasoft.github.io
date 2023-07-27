# EE\_INFO\_EX

检索或设置用于 EmEditor 的信息参数之一的值。你能明确地发送该消息或用 [Editor\_DocInfoEx](../macro/editor_docinfoex) 内联函数。

EE\_INFO\_EX

wParam = (WPARAM)(INFO\_EX\_DATA\*)pInfo;

lParam = 0;

## 参数

_pInfo_

指针指向 [INFO\_EX\_DATA 结构](../structure/info_ex_data)。

## 返回值

取决于指定的参数。

## 支持版本

支持 EmEditor Professional v21.8 或之后的版本。
