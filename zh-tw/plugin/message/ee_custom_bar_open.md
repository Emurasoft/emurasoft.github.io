# EE\_CUSTOM\_BAR\_OPEN

打開自訂分欄。如果在發送該消息前已經打開了一個自訂分欄，EmEditor 會關閉該自訂分欄并打開一個新的自訂分欄。您能明確地發送該消息或用 [Editor\_CustomBarOpen](../macro/editor_custombaropen) 內嵌函式。

EE\_CUSTOM\_BAR\_OPEN

wParam = 0;

lParam = (LPCTSTR) (LPCTSTR) pCustomBarInfo;

## 參數

_pCustomBarInfo_

指針指向 [CUSTOM\_BAR\_INFO 結構](../structure/custom_bar_info)。

## 返回值

返回值是一個自訂分欄 ID。這個 ID 是必要的當用 EE\_CUSTOM\_BAR\_CLOSE 消息來關閉該自訂分欄時。如果消息不成功，返回值則是零。

## 支持版本

支持 EmEditor 6.00 或之後的版本。
