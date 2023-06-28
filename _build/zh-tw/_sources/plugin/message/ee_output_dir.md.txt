# EE\_OUTPUT\_DIR

為輸出列設置當前目錄。您能明確地發送該消息或用 [Editor\_OutputDir](../macro/editor_outputdir) 內嵌函式。

EE\_OUTPUT\_DIR

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szCurrDir;

## 參數

_szCurrDir_

> 指定當前目錄。該信息是必需的如果文本含有一個只能從當前目錄上跳轉的、可點擊的相對路徑。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。