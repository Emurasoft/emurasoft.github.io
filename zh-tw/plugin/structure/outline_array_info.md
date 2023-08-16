# OUTLINE\_ARRAY\_INFO

用於
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray)
內嵌函式 ( [EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 消息) 中。

```
typedef struct _OUTLINE_ARRAY_INFO {
	int nVersion;
	UINT nFlags;
	INT_PTR nStartLine;
	INT_PTR nCount;
	BYTE* pLevelData;
} SET_INFO;
```

## 欄位

_nVersion_

已保留。必須是 1。

_nFlags_

已保留。必須是 0。

_nCount_

指定多行的行數。

_pLevelData_

指定一個決定大綱級別的位元數組。

## 支持版本

支持 EmEditor 13 或之後的版本。
