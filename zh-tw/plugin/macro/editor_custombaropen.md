# Editor\_CustomBarOpen

打開自訂顯示條。如果在發送該消息前已經打開了一個自訂顯示條，EmEditor 會關閉該自訂顯示條并打開一個新的自訂顯示條。您能直接用該內嵌函式或明確地發送 [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) 消息。

Editor\_CustomBarOpen( HWND hwnd, CUSTOM\_BAR\_INFO\* pCustomBarInfo );

## 參數

_pCustomBarInfo_

指標至 [CUSTOM\_BAR\_INFO 結構](../structure/custom_bar_info)。

## 返回值

返回值是一個自訂顯示條 ID。這個 ID 是必要的當用 Editor\_CustomBarClose 內嵌函式來關閉該自訂顯示條時。如果消息不成功，返回值則是零。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
