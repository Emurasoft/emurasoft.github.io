# Editor\_LoadFileW

把一個指定檔案載入到 EmEditor 中。檔案名稱由一個 Unicode 字串指定。您能直接用該內嵌函式或明確地發送
[EE\_LOAD\_FILEW](../message/ee_load_filew) 消息。

Editor\_LoadFileW( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCWSTR szFileName
);

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pLoadFileInfo_

> 指標至一個 [LOAD\_FILE\_INFO](../structure/load_file_info) 結構。如果該參數為空 (NULL)，Editor\_LoadFileW 會通過屬性中預設的方式打開一個檔案。

_szFileName_

> 用位元指定一個完整路徑檔案名稱。如果指定了一個不存在的檔案，Editor\_LoadFileW 會失敗。

## 返回值

> 如果命令被啟用，返回值就不是零。如果命令沒有被啟用，返回值是零。