# EE\_GET\_UNICODE\_NAME

检索指定字符或字符串的 Unicode 名。你能明确地发送该消息或用 [Editor\_GetUnicodeName 内联函数](../macro/editor_getunicodename)。

```
EE_GET_UNICODE_NAME
wParam = (WPARAM)(UNICODE_NAME_INFO*)pUNI;
lParam = 0;
```

## 参数

_pUNI_

指定指针指向 [UNICODE\_NAME\_INFO 结构](../structure/unicode_name_info)。

## 返回值

如果 UNICODE\_NAME\_INFO 结构的 _cchBuf_ 字段是零，那返回值则是用字符数表示的一个会接收文本的缓冲区的必需大小。

## 版本

支持 EmEditor Professional 19.1 或之后的版本。
