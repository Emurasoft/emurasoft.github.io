# ACTIVE\_STRING\_INFO

用於 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息。

```
typedef struct _ACTIVE_STRING_INFO {
	UINT cbSize;
	LPWSTR pBuf;
	UINT cchBuf;
	UINT nFlags;
} ACTIVE_STRING_INFO;
```

## 成員

_cbSize_

以字節為單位的數據結構大小。在發送 [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) 消息之前，把這個成員設為 sizeof( ACTIVE\_STRING\_INFO )。

_pBuf_

指定要接收主動字串的緩衝區。

_cchBuf_

用字元數指定緩衝區大小。

_nFlags_

目前不使用。

## 版本

支持 EmEditor Professional 16.9 或之後的版本。
