# Editor\_RearrangeColumns

重排 CSV 欄。你能直接用該內嵌函式或明確地發送 [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) 消息。

Editor\_RearrangeColumns( HWND hwnd, UINT nColumnArraySize, const INT\* piColumn );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nSize_

> 指定在 _piColumn_ 參數中指定的欄數。

_piColumn_

> 指定一個整數陣列，指示要重新排列的欄的順序。例如，"0, 2, 4" 表示結果將包括原始 CSV 文檔的第一欄、第三欄和第五欄。

## 返回值

> 如果消息成功，則返回值為零。如果消息失敗，則返回值非零。

## 版本

> 支持 EmEditor Professional v22.1 或之後的版本。
