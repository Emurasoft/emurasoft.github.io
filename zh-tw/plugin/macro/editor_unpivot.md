# Editor\_Unpivot

通過壓平合併 CSV 數據將欄轉換為列。你能直接用該內嵌函式或明確地發送 [EE\_UNPIVOT](../message/ee_unpivot) 消息。

HRESULT Editor\_Unpivot( HWND hwnd, LPCWSTR pszSelect, LPCWSTR pszAttrLabel, LPCWSTR pszValueLabel, int nFooter );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控點。

_pszSelect_

> 指定用於選擇要取消樞紐的欄的字串。例如，"2-5", "3-", "1,3,5"。此欄位不能為空。

_pszAttrLabel_

> 指定要建立的屬性欄的標題標籤。

_pszValueLabel_

> 指定要建立的值欄的標題標籤。

_nFooter_

> 指定頁腳中的列數。頁腳列不會被轉換。

## 返回值

> 如果失敗，返回值為負值。

## 版本

> 支持 EmEditor Professional 21.4 或之後的版本。