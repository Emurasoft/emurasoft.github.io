# EE\_CONVERT\_CSV

转换当前文档的 CSV 格式。你能明确地发送该消息或用 [Editor\_ConvertCsv](../macro/editor_convertcsv) 内联函数。

EE\_EDIT\_COLUMN

wParam = (WPARAM)(CONVERT\_CSV\_INFO\*)pInfo;

lParam = 0;

## 参数

_pInfo_

指定指针指向 [CONVERT\_CSV\_INFO](../structure/convert_csv_info) 结构。

## 返回值

如果成功，返回值为 S\_OK。

## 版本

支持 EmEditor Professional 19.8 或之后的版本。
