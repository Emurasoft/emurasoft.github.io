# EE\_SAVE\_FILEA

保存文本到一個指定的檔案中。檔案名稱被指定為一個 ANSI 字符串。您能明確地發送該消息或用
[Editor\_SaveFileA](../macro/editor_savefilea) 內嵌函式。

EE\_SAVE\_FILEA

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPSTR) szFileName;

## 參數

_bReplace_

指定 TRUE 如果文本用一個指定的名稱保存，并且 EmEditor 保留該檔案名。另外，顯示在 EmEditor 視窗上的標題也會被改變。指定 FALSE 如果保存了該文本的副本，并且 EmEditor 所保留的檔案名稱將不會被改變。

_szFileName_

用位元指定一個完整的路徑檔案名稱。

## 返回值

如果消息成功，返回值不是零。如果消息不成功，返回值是零。
