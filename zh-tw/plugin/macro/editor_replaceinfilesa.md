# Editor\_ReplaceInFilesA

在指定位置的多個檔案中搜尋一個 ANSI 字串。您能直接用該內嵌函式或明確地發送 [EE\_REPLACE\_IN\_FILESA message](../message/ee_replace_in_filesa).

Editor\_ReplaceInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pGrepInfo_

> 指定一個指標至 [GREP\_INFOW \
> 結構](../structure/grep_infow)。

## 返回值

> 返回 FALSE 如果使用者中止，不然，返回 TRUE。

## 支持版本

> 支持 EmEditor 4.02 或之後的版本。
