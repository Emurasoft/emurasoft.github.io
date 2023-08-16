# UNPIVOT\_INFO

用于 [EE\_UNPIVOT](../message/ee_unpivot) 消息中。

```
typedef struct _UNPIVOT_INFO {
	UINT cbSize;
	UINT nFlags;
	LPCWSTR pszSelect;
	LPCWSTR pszAttrLabel;
	LPCWSTR pszValueLabel;
	int nFooter;
} UNPIVOT_INFO;
```

## 字段

_cbSize_

指定 sizeof( UNPIVOT\_INFO )。

_nFlags_

不使用。必须为 0。

_pszSelect_

指定用于选择要逆透视的列的字符串。例如，"2-5", "3-", "1,3,5"。此字段不能为空。

_pszAttrLabel_

指定要创建的属性列的标题标签。

_pszValueLabel_

指定要创建的值列的标题标签。

_nFooter_

指定页脚中的行数。页脚行不会被转换。

## 版本

支持 EmEditor Professional 21.4 或之后的版本。
