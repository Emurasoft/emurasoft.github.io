# TIP\_INFO

用于 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息。

```
typedef struct _TIP_INFO {
	UINT cbSize;
	LPCWSTR pszTip;
	POINT_PTR ptCaret;
	POINT ptDev;
	UINT nFlags;
} TIP_INFO;
```

## 成员

_cbSize_

以字节为单位的数据结构大小。在发送 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息之前，把这个成员设为sizeof ( TIP\_INFO )。

_pszTip_

指定在工具提示中显示的文本。文本长度不能超过 3,999 个字符。该字符串可包含以这种格式指定的可点击文本："<a href="url">可点击文本</a>"。

_ptCaret_

目前不使用。

_ptDev_

目前不使用。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| SHOW\_TIP\_ACTIVE\_STRING | 在鼠标悬停的活动字符串处显示工具提示。 |
| SHOW\_TIP\_CURRENT\_CARET | 在插入符号位置显示工具提示。 |
| SHOW\_TIP\_CURRENT\_MOUSE | 在鼠标指针位置显示工具提示。 |
| SHOW\_TIP\_HIDE | 如果已经显示，隐藏工具提示。 |

## 版本

支持 EmEditor Professional 16.9 或之后的版本。
