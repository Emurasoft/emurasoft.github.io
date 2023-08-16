# QUERY\_STRING\_INFO

用于 [EE\_QUERY\_STRING\_EX 消息](../message/ee_query_string_ex) 中。

typedef struct \_QUERY\_STRING\_INFO {

UINT cbSize;

UINT nCmdID;

UINT nFlags;

UINT cchBuf;

LPWSTR pBuf;

} QUERY\_STRING\_INFO;

## 成员

_cbSize_

以字节为单位的数据结构大小。把这个成员设为 sizeof( QUERY\_STRING\_INFO )。

_nCmdID_

指定一个表示要执行的命令 ID 的整数。只能使用下列命令。详细信息请访问
**[命令参考](../../cmd/index)**。

|     |     |     |
| --- | --- | --- |
| nID | 命令名称 | 返回值 |
| 4609 到 4609 + 63 | [**最近文档列表**](../../cmd/file/file_mru_file1) | 文件路径和名称 |
| 4864 到 4864 + 63 | [**要插入的最近文件列表**](../../cmd/file/file_mru_insert1) | 文件路径和名称 |
| 4992 到 4992 + 63 | [**最近文件夹列表**](../../cmd/file/file_mru_folder1) | 文件路径和名称 |
| 5376 到 5376 + 255 | **[文档列表命令](../../cmd/window/window_menu)** | 窗口标题 |
| 5632 到 5632 + 255 | **[插件列表命令](../../cmd/tools/plug_in1)** | 插件文件名称 |
| 6656 到 6656 + 255 | [**要重新载入的编码列表命令**](../../cmd/file/file_reload_defined) | 编码名称 |
| 7680 到 7680 + 255 | [**要保存的编码列表**](../../cmd/file/file_save_defined) | 编码名称 |
| 9216 到 9216 + 1023 | **[宏列表命令](../../cmd/macros/macro1)** | 宏路径和名称 |

_nFlags_

指定以下值之一。

|     |     |
| --- | --- |
| QUERY\_STRING\_LONG\_TITLE | 指定需要该字符串的长版本。 |
| QUERY\_STRING\_SHORT\_TITLE | 指定需要该字符串的简短版本。 |

_cchBuf_

指定以字符为单位的缓冲区大小。

_pBuf_

指定用于检索字符串的缓冲区。

## 支持版本

支持 EmEditor Professional Version 20.6 或之后的版本。
