# EE\_QUERY\_STRING

查询与指定的命令相关联的字符串。你能明确地发送该消息或用 [Editor\_QueryString](../macro/editor_querystring) 内联函数。

EE\_QUERY\_STRING

wParam = (WPARAM) MAKEWPARAM( nCmdID, bShortTitle );

lParam = (LPARAM) (LPWSTR) psz;

## 参数

_nCmdID_

> 指定一个表示要执行的命令 ID 的整数。只能使用下列命令。详细信息请访问
> **[命令参考](../../cmd/index)**。
>
> |     |     |     |
> | --- | --- | --- |
> | nID | 命令名称 | 返回值 |
> | 4609 到 4609 + 63 | [**最近文档列表**](../../cmd/file/file_mru_file1) | 文件路径和名称 |
> | 4864 到 4864 + 63 | [**要插入的最近文件列表**](../../cmd/file/file_mru_insert1) | 文件路径和名称 |
> | 4992 到 4992 + 63 | [**最近文件夹列表**](../../cmd/file/file_mru_folder1) | 文件路径和名称 |
> | 5376 到 5376 + 255 | **[文档列表命令](../../cmd/window/window_menu)** | 窗口标题 |
> | 5632 到 5632 + 255 | **[插件列表命令](../../cmd/tools/plug_in1)** | 插件文件名称 |
> | 6656 到 6656 + 255 | [**要重新载入的编码列表命令**](../../cmd/file/file_reload_defined) | 编码名称 |
> | 7680 到 7680 + 255 | [**要保存的编码列表**](../../cmd/file/file_save_defined) | 编码名称 |
> | 9216 到 9216 + 1023 | **[宏列表命令](../../cmd/macros/macro1)** | 宏路径和名称 |

_bShortTitle_

> 指定是否在特定命令中需要字符串的简短版本。

_psz_

> 指定要检索字符串的缓冲区。

## 返回值

> 如果命令 ID 有效，返回值是非零。否则的话，返回值是零。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。