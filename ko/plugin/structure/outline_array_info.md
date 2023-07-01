# OUTLINE\_ARRAY\_INFO

[Editor\_SetOutlineArray](../macro/editor_setoutlinearray)
인라인 함수( [EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 메시지)에 의해 사용됩니다.

typedef struct \_OUTLINE\_ARRAY\_INFO {

int nVersion;

UINT nFlags;

INT\_PTR nStartLine;

INT\_PTR nCount;

BYTE\* pLevelData;

} SET\_INFO;

## 필드

_nVersion_

> 예정되어 있습니다. 반드시 1이어야 합니다.

_nFlags_

> 예정되어 있습니다. 반드시 0이어야 합니다.

_nCount_

> 다중 선의 수를 지정합니다.

_pLevelData_

> 개요 수준을 지정하는 BYTE의 배열을 지정합니다.

## 버전

> EmEditor 버전 13 이상에서만 지원됩니다.
