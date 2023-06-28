# EE\_INSERT\_FILEA

在光標處插入指定檔案內容。檔案名用一個 ANSI 字符串指定。您能明確地發送該消息或用
[Editor\_InsertFileA](../macro/editor_insertfilea) 內嵌函式。

EE\_INSERT\_FILEA

wParam = (WPARAM) (LOAD\_FILE\_INFO\*) pLoadFileInfo;

lParam = (LPARAM) (LPCSTR) szFileName;

## 參數

_pLoadFileInfo_

> 指針指向一個 [LOAD\_FILE\_INFO](../structure/load_file_info) 結構。如果該參數為空，EE\_INSERT\_FILEA 會通過屬性中預設的方式打開一個檔案。

_szFileName_

> 指定一個完整路徑的檔案名稱。如果指定了一個不存在的檔案，EE\_INSERT\_FILEA 會失敗。

## 返回值

> 如果命令成功，返回值就不是零。如果命令不成功，返回值是零。