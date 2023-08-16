# INFO\_EX\_DATA

用於 [**EE\_INFO\_EX** 消息](../message/ee_info_ex)。

typedef struct \_INFO\_EX\_DATA {

UINT cbSize;

UINT nCmd;

HEEDOC hDoc;

LPARAM lParam;

} INFO\_EX\_DATA;

## 欄位

_cbSize_

必須是 sizeof(INFO\_EX\_DATA)。

_nCmd_

指定要檢索或設定的參數。請參閱 [**EE\_INFO** 消息](../message/ee_info) 的命令清單。

_hDoc_

指定目標文件的控點。如果指定 NULL，則目前使用中的文件將成為目標。根據 _nCmd_，也有可能不使用該欄位。

_lParam_

取決於指定的參數。

## 版本

支持 EmEditor Professional v21.8 或之後的版本。
