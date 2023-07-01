# EE\_CUSTOM\_BAR\_CLOSE

关闭自定义分栏。你能明确地发送该消息或用
[Editor\_CustomBarClose](../macro/editor_custombarclose) 内联函数。

EE\_CUSTOM\_BAR\_CLOSE

wParam = nCustomBarID;

lParam = 0;

## 参数

_nCustomBarID_

> 指定要关闭的自定义分栏。这是从 EE\_CUSTOM\_BAR\_OPEN 消息中得到的返回值。

## 返回值

> 如果消息成功，返回值为 TRUE。如果消息不成功，返回值是 FALSE。

## 支持版本

> 支持 EmEditor 6.00 或之后的版本。
