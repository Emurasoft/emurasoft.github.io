# EE\_REG\_SET\_VALUE

根据 EmEditor 的设定，设一个值到注册表或一个 INI 文件中。你能明确地发送该消息或用 [Editor\_RegSetValue](../macro/editor_regsetvalue) 内联函数。

EE\_REG\_SET\_VALUE

wParam = 0;

(REG\_SET\_VALUE\_INFO\*)lParam = pRegSetValueInfo;

## 参数

_pRegSetValueInfo_

> 指针指向 [REG\_SET\_VALUE\_INFO 结构](../structure/reg_set_value_info)。

## 返回值

> 如果消息成功，返回值是 ERROR\_SUCCESS。
>
> 如果消息不成功，返回值是一个在 Winerror.h 中被定义的非零的错误代码。

## 支持版本

支持 EmEditor 7.00 或之后的版本。
