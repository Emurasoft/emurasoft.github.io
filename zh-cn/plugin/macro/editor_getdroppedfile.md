# Editor\_GetDroppedFile

检索最近拖放的文件。你能直接用该内联函数或明确地发送 [EE\_GET\_DROPPED\_FILE](../message/ee_get_dropped_file)
消息。

Editor\_GetDroppedFile( HWND hwnd, int nIndex, LPWSTR pszBuf );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nIndex_

指定拖放文件的索引。应指定从 0 开始的索引。如果指定 -1，那拖放文件的总数会被返回。

_pszBuf_

指定接收拖放文件名称的一个缓冲区。缓冲区大小必须是 MAX\_PATH 的以字节为单位的值。这个参数可以为空 (NULL)，如果 -1 在 nIndex 中被指定的话。

## 返回值

返回值为非零值如果拖放文件存在在指定的索引中。如果在 nIndex 中指定 -1，返回值是拖放文件的总数。

## 支持版本

支持 EmEditor 8.00 或之后的版本。
