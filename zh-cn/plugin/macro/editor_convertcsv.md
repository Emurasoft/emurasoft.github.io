# Editor\_ConvertCsv

转换当前文档的 CSV 格式。你能直接用该内联函数或明确地发送 [EE\_CONVERT\_CSV](../message/ee_convert_csv) 消息。

HRESULT Editor\_ConvertCsv( HWND hwnd, int iDestMode, UINT nFlags = 0, int nSepCount = 0, const int\* pcxSepWidths = NULL );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_iDestMode_

指定要将当前文档转换为 CSV 格式的索引。0 表示固定宽度的列格式（非 CSV）。1 表示“自定义”对话框中 “CSV” 页面上的第一个定义的格式（默认情况下是“逗号分隔”）。

_nFlags_

你能指定一个下列值的组合。

| 值 | 含义 |
| --- | --- |
| CSV\_HALF\_WIDTH | 假定所有字符为半角字符以提高速度。 |
| CSV\_DISCARD\_UNDO | 丢弃撤消信息以提高速度。 |

_nSepCount_

如果当前文档是非 CSV 文档，并且要将当前固定列宽的文档转换为 CSV 文档，则此参数指定分隔符数，并且它必须与在 _pcxSepWidths_ 参数中指定的数组大小相同。如果当前文档是 CSV 文档，则可忽略此参数。

_pcxSepWidths_

如果 _nSepCount_ 参数不是零，则指定表示分隔符之间的宽度的整数数组。

## 返回值

如果成功，返回值为 S\_OK。

## 版本

支持 EmEditor Professional 19.8 或之后的版本。
