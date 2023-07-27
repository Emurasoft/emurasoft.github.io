# EE\_CONVERT\_CSV

轉換目前的文檔的 CSV 格式。你能明確地發送該消息或用 [Editor\_ConvertCsv](../macro/editor_convertcsv) 內嵌函式。

EE\_EDIT\_COLUMN

wParam = (WPARAM)(CONVERT\_CSV\_INFO\*)pInfo;

lParam = 0;

## 參數

_pInfo_

指定指針指向 [CONVERT\_CSV\_INFO](../structure/convert_csv_info) 結構。

## 返回值

如果成功，返回值為 S\_OK。

## 版本

支持 EmEditor Professional 19.8 或之後的版本。
