# SEL\_INFO

Editor\_GetMultiSel 인라인 함수
( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) 메시지)에 의해 사용됩니다.

typedef struct \_SEL\_INFO {

POINT\_PTR ptStart;

POINT\_PTR ptEnd;

} SET\_INFO;

## 필드

_ptStart_

> 선택 영역의 시작 지점을 지정합니다.

_ptEnd_

> 선택 영역의 끝 지점을 지정합니다.

## 버전

> EmEditor 버전 13 이상에서만 지원됩니다.