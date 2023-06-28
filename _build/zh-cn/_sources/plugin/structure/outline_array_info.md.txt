# OUTLINE\_ARRAY\_INFO

用于
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray)
内联函数 ( [EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 消息) 中。

typedef struct \_OUTLINE\_ARRAY\_INFO {

int nVersion;

UINT nFlags;

INT\_PTR nStartLine;

INT\_PTR nCount;

BYTE\* pLevelData;

} SET\_INFO;

## 字段

_nVersion_

> 已保留。必须是 1。

_nFlags_

> 已保留。必须是 0。

_nCount_

> 指定多行的行数。

_pLevelData_

> 指定一个决定大纲级别的字节数组。

## 支持版本

> 支持 EmEditor 13 或之后的版本。