# UNPIVOT\_INFO

用於 [EE\_UNPIVOT](../message/ee_unpivot) 消息中。

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

## 欄位

_cbSize_

指定 sizeof( UNPIVOT\_INFO )。

_nFlags_

不使用。必須為 0。

_pszSelect_

指定用於選擇要取消樞紐的欄的字串。例如，"2-5", "3-", "1,3,5"。此欄位不能為空。

_pszAttrLabel_

指定要建立的屬性欄的標題標籤。

_pszValueLabel_

指定要建立的值欄的標題標籤。

_nFooter_

指定頁腳中的列數。頁腳列不會被轉換。

## 版本

支持 EmEditor Professional 21.4 或之後的版本。
