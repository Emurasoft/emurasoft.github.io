# EE\_LOAD\_FILEA

把一個指定檔案載入到 EmEditor 中。檔案名稱由一個 ANSI 字符串指定。您能明確地發送該消息或用
[Editor\_LoadFileA](../macro/editor_loadfilea) 內嵌函式。

```
EE_LOAD_FILEA
wParam = (WPARAM) (LOAD_FILE_INFO*) pLoadFileInfo;
lParam = (LPARAM) (LPCSTR) szFileName;
```

## 參數

_pLoadFileInfo_

指針指向一個 [LOAD\_FILE\_INFO](../structure/load_file_info) 結構。如果該參數為空 (NULL)，EE\_LOAD\_FILEA 會通過屬性中預設的方式打開一個檔案。

_szFileName_

用位元指定一個完整路徑檔案名稱。如果指定了一個不存在的檔案，EE\_LOAD\_FILEA 會失敗。

## 返回值

如果命令被啟用，返回值就不是零。如果命令沒有被啟用，返回值是零。
