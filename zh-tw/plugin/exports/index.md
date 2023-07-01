# 導出函數

|     |     |
| --- | --- |
| OnCommand( HWND hwnd ) | 外掛程式已從功能表或工具列中被選擇。 |
| QueryStatus( HWND hwnd, LPBOOL pbChecked ) | 查詢外掛程式的狀態，命令是否被啟用以及外掛程式是否在檢查狀態。 |
| OnEvents( HWND hwnd, UINT nEvent, LPARAM lParam ) | 當一個狀態被改變時，可以用 [事件](../event/index) 參數調用該函數。 |
| GetMenuTextID() | 檢索外掛程式功能表項目文字的資源 ID。 |
| GetStatusMessageID() | 檢索用 \\n 把工具列上的提示文字與狀態列文字合併的資源 ID。 |
| GetBitmapID() | 獲得顯示在工具列上的外掛程式的位圖資源 ID。 |
| PlugInProc( HWND hwnd, UINT nMsg, WPARAM wParam, LPARAM lParam ) | 用 [外掛程式消息](../plugin_message/index) 來檢索或設置設定。 |

這些導出函數必須通過這個順序在一個 DEF 檔案中定義。當您編譯它們時，您需要選擇 \_stdcall 作為調用方式。有關更多外掛程式示例的信息，請訪問 EmEditor 網站的資源庫。

