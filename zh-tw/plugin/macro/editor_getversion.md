# Editor\_GetVersion

返回版本號。您能直接用該內嵌函式或明確地發送 [EE\_GET\_VERSION](../message/ee_get_version)
消息。

Editor\_GetVersion( HWND hwnd );

Editor\_GetVersionEx( HWND hwnd, int\* pnProductType );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pnProductType_

指定一個指標至整數值。這個消息返回下列值之一。

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## 返回值

返回被乘以 10000 的版本號。例如，如果版本號為 25.1.907，則返回值將為 251907。
