# Editor\_InsertFileA

在游標處插入指定檔案內容。檔案名用一個 ANSI 字串指定。您能直接用該內嵌函式或明確地發送
[EE\_INSERT\_FILEA 消息](../message/ee_insert_filea)。

Editor\_InsertFileA( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCSTR
szFileName );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pLoadFileInfo_

指標至一個 [LOAD\_FILE\_INFO](../structure/load_file_info) 結構。如果該參數為空，Editor\_InsertFileA 會通過屬性中預設的方式打開一個檔案。

_szFileName_

指定一個完整路徑的檔案名稱。如果指定了一個不存在的檔案，Editor\_InsertFileA 會失敗。

## 返回值

如果命令成功，返回值就不是零。如果命令不成功，返回值是零。
