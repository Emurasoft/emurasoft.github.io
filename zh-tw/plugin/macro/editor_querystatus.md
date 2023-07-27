# Editor\_QueryStatus

查詢命令的狀態，無論命令是否被啟用，也不管命令是否處于被選中的狀態。您能直接用該內嵌函式或明確地發送 [EE\_QUERY\_STATUS](../message/ee_query_status) 消息。

Editor\_QueryStatus( HWND hwnd, UINT nCmdID, BOOL\* pbChecked );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nCmdID_

狀態被查詢的命令的標識符。請參考
[命令 ID](../cmdid/index)。

_pbChecked_

指標至一個接收勾選狀態的變量 (TRUE 表示所選命令已被選中，FALSE 則表示所選命令沒有被勾選) 。

## 返回值

如果命令被啟用，返回值就不是零。如果命令沒有被啟用，返回值是零。
