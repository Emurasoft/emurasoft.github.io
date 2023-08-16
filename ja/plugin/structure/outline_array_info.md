# OUTLINE\_ARRAY\_INFO

[EE\_SET\_OUTILNE\_ARRAY](../message/ee_set_outline_array) メッセージ ( [Editor\_SetOutlineArray](../macro/editor_setoutlinearray)
インライン関数) で使用します。

```
typedef struct _OUTLINE_ARRAY_INFO {
	int nVersion;
	UINT nFlags;
	INT_PTR nStartLine;
	INT_PTR nCount;
	BYTE *pLevelData;
} SET_INFO;
```

## フィールド

_nVersion_

予約済み。1 を指定する必要があります。

_nFlags_

予約済み。0 を指定する必要があります。

_nCount_

複数行の行数を指定します。

_pLevelData_

アウトライン レベルを指定する BYTE 配列を指定します。

## バージョン

Version 13 以上で利用できます。
