# INFO\_EX\_DATA

用于 [**EE\_INFO\_EX** 消息](../message/ee_info_ex)。

typedef struct \_INFO\_EX\_DATA {

UINT cbSize;

UINT nCmd;

HEEDOC hDoc;

LPARAM lParam;

} INFO\_EX\_DATA;

## 字段

_cbSize_

> 必须是 sizeof(INFO\_EX\_DATA)。

_nCmd_

> 指定要检索或设置的参数。请参阅 [**EE\_INFO** 消息](../message/ee_info) 的命令列表。

_hDoc_

> 指定目标文档的句柄。如果指定 NULL，则当前的活动文档将成为目标。根据 _nCmd_，也有可能不使用该字段。

_lParam_

> 取决于指定的参数。

## 版本

> 支持 EmEditor Professional v21.8 或之后的版本。
