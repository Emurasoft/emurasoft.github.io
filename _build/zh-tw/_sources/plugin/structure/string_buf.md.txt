# STRING\_BUF

用於 [EE\_INFO 消息](../message/ee_info) 中。

typedef struct \_STRING\_BUF {

LPWSTR pBuf;

UINT cchBuf;

} STRING\_BUF;

## 成員

_pBuf_

> 指定用於檢索字串的緩沖區。

_cchBuf_

> 指定以字元為單位的緩沖區大小。

## 支持版本

> 支持 EmEditor Professional Version 20.6 或之後的版本。