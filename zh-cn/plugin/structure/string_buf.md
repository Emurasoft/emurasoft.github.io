# STRING\_BUF

用于 [EE\_INFO 消息](../message/ee_info) 中。

```
typedef struct _STRING_BUF {
	LPWSTR pBuf;
	UINT cchBuf;
} STRING_BUF;
```

## 成员

_pBuf_

指定用于检索字符串的缓冲区。

_cchBuf_

指定以字符为单位的缓冲区大小。

## 支持版本

支持 EmEditor Professional Version 20.6 或之后的版本。
