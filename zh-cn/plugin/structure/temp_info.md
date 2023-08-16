# TEMP\_INFO

用于 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息以及 [EVENT\_TEMP\_SAVING 事件](../event/index) 中。

```
typedef struct _TEMP_INFO {
	size_t cbSize;
	LPCWSTR pszTempText;
	LPCWSTR pszTitle;
	LPCWSTR pszIconPath;
	LPCWSTR pszConfig;
	POINT_PTR ptInitialCaret;
	UINT nID;
	UINT nEncoding;
	UINT nFlags;
} TEMP_INFO;
```

## 成员

_cbSize_

用字节数表示该数据结构的大小。把这个构成部分设为 sizeof( TEMP\_INFO ) 在发送 [EE\_EDIT\_TEMP](../message/ee_edit_temp) 消息前。

_pszTempText_

指定要打开一个新文档的内存中的临时文本。

_pszTitle_

指定新文档的标题。

_pszIconPath_

指定你想要用作新文档的图标路径以及文件名。

_pszConfig_

指定新文档应使用的配置名称。

_ptInitialCaret_

指定初始光标位置。

_nID_

指定一个 ID 当你想要激活或关闭临时文本时。

_nEncoding_

指定文件的编码。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | 打开临时文本如果 nID 为零。激活已存在的临时文本如果 nID 不是零。 |
| TEMP\_INFO\_CLOSE | 关闭用 nID 指定的临时文本。 |
| TEMP\_INFO\_SAVE | 保存用 nID 指定的临时文本。 |

## 版本

支持 EmEditor ９.00 或之后的版本.
