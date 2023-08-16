# ACTIVE\_STRING\_INFO

用于 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息。

```
typedef struct _ACTIVE_STRING_INFO {
	UINT cbSize;
	LPWSTR pBuf;
	UINT cchBuf;
	UINT nFlags;
} ACTIVE_STRING_INFO;
```

## 成员

_cbSize_

以字节为单位的数据结构大小。在发送 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息之前，把这个成员设为 sizeof( ACTIVE\_STRING\_INFO )。

_pBuf_

指定要接收活动字符串的缓冲区。

_cchBuf_

用字符数指定缓冲区大小。

_nFlags_

目前不使用。

## 版本

支持 EmEditor Professional 16.9 或之后的版本。
