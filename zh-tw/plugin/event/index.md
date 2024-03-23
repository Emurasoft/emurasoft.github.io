# 事件

|     |     |
| --- | --- |
| EVENT\_CARET\_MOVED | 光標位置被移動。 |
| EVENT\_CHANGE | 文本被更改。 |
| EVENT\_CHAR | 插入一個字符。LOWORD (lParam) 表示插入的 Unicode 字符代碼。 |
| EVENT\_CLOSE | 在關閉 EmEditor 之前或該外掛程式被釋放前立即調用。一個外掛程式應該釋放資源，并使 DLL 檔案可以被刪除。 [OnEvents 函數](../exports/index) 的第一個參數 hwnd 會是 NULL。這個事件不代表該外掛程式實際上會被釋放。 |
| EVENT\_CLOSE\_FRAME | 當關閉一個 EmEditor 框架視窗時被調用 (支持 EmEditor 5.00 或之後的版本) 。 |
| EVENT\_CONFIG\_CHANGED | 當前配置屬性被更改。 |
| EVENT\_CREATE | 在 啟動 EmEditor 或該外掛程式被加載時立即調用。LOWORD(lParam) 代表該外掛程式本身的命令 ID。 |
| EVENT\_CREATE\_FRAME | 當新建一個 EmEditor 框架視窗時被調用。這個事件在啟用或禁用標簽頁時也會被調用。LOWORD(lParam) 代表該外掛程式本身的命令 ID (支持 EmEditor 5.00 或之後的版本) 。 |
| EVENT\_CUSTOM\_BAR\_CLOSED | 當關閉一個自訂分欄時被調用。EmEditor 調用 DestroyWindow() 到客戶端視窗上，當一個自訂分欄被關閉。lParam 代表一個指針指向 [CUSTOM\_BAR\_CLOSED\_INFO 結構](../structure/custom_bar_close_info) (支持 EmEditor 6.00 或之後的版本) 。 |
| EVENT\_CUSTOM\_BAR\_CLOSING | 當關閉一個自訂分欄時被調用。lParam 代表存儲個指針到 [CUSTOM\_BAR\_CLOSED\_INFO 結構](../structure/custom_bar_close_info) 中 (支持 EmEditor 6.00 或之後的版本) 。 |
| EVENT\_DOC\_CLOSE | 當一個文檔要被關閉時被調用。lParam 代表存儲一個處理 (HEEDOC) 到正在關閉的文檔中 (支持 EmEditor 5.00 或之後的版本) 。 |
| EVENT\_DOC\_SEL\_CHANGED | 當一個活動的文檔發生更改時被調用 (支持 EmEditor 5.00 或之後的版本) 。 |
| EVENT\_DROPPED | 一個檔案被拖放到 EmEditor 框架視窗中。 |
| EVENT\_FILE\_OPENED | 打開一個檔案。 |
| EVENT\_HISTORY | 每次更改文本時被調用。lParam 代表存儲一個指針到 HISTORY\_INFO 結構中。 |
| EVENT\_IDLE | 當閑置時調用。 (支持 EmEditor 6.00 或之後的版本) 。 |
| EVENT\_KILL\_FOCUS | 失去焦點。 |
| EVENT\_LANGUAGE | 更改 UI 語言。 |
| EVENT\_MODIFIED | 修改狀態被改變。 |
| EVENT\_SAVING | 文檔要被保存時。lParam 代表存儲一個處理 (HEEDOC) 到正被保存的文檔中 (支持 EmEditor 8.00 或之後的版本) 。 |
| EVENT\_SCROLL | 滾動欄位置被更改。 |
| EVENT\_SEL\_CHANGED | 文本的選區被更改。 |
| EVENT\_SET\_FOCUS | 焦點已被設定。 |
| EVENT\_TAB\_MOVED | 當移動一個標簽頁時被調用。 |
| EVENT\_TEMP\_SAVING | 當用戶正要保存一個臨時文檔時被調用。該外掛程式負責保存檔案。lParam 代表存儲一個指針到 [TEMP\_INFO 結構](../structure/temp_info) 中。 |
| EVENT\_TOOLBAR\_CLOSED | 當關閉一個自訂工具列時被調用。與 EVENT\_CUSTOM\_BAR\_CLOSED 消息不同，EmEditor 不毀壞客戶端視窗。lParam 代表存儲一個指針到 [TOOLBAR\_INFO 結構](../structure/toolbar_info) 中 (支持 EmEditor 7.00 或之後的版本) 。 |
| EVENT\_TOOLBAR\_SHOW | 當顯示或隱藏一個自訂工具列時被調用 (即當 RBBS\_HIDDEN 樣式被切換時) 。lParam 代表存儲一個指針到 [TOOLBAR\_INFO 結構](../structure/toolbar_info) 中 (支持 EmEditor 7.00 或之後的版本) 。 |
| EVENT\_UI\_CHANGED | 調用當 UI 變更時。<br> changed. lParam 代表下列標志的組合: UI\_CHANGED\_LANGUAGE 以及 UI\_CHANGED\_TOOLBARS。 |

通過 [OnEvents](../exports/index) 函數，這些事件被用作 nEvents 參數。

這些常數在頭檔案 (plugin.h) 中被定義。

