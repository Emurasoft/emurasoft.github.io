# Editor_GetSelLength

检索所选文本的长度。你可以使用此内联函数，或显式发送 [EE_GET_SEL_LENGTH](../message/ee_get_sel_length) 消息。

nLen = Editor_GetSelLength( HWND hwnd, size_t nMaxLen = 0 );

## 参数

_hwnd_

指定 EmEditor 的视图或框架窗口句柄。

_nMaxLen_

指定最大长度。如果长度超过此值，则返回该值。

## 返回值

返回值为所选文本的长度。

## 版本

支持 EmEditor Professional 26.1 或更新版本。