# Editor\_GetAccelArray

바로가기 키의 배열을 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_ACCEL\_ARRAY](../message/ee_get_accel_array) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetAccelArray( HWND hwnd, ACCEL\* pAccel, UINT nBufSize );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nBufSize_

> ACCEL로 바로가기 키 배열을 수신할 버퍼의 크기를 지정합니다.

_pAccel_

> ACCEL 구조의 배열을 수신할 버퍼에 대한 포인터를 지정합니다.

## 반환 값

> 반환 값은 ACCEL로 바로가기 키 배열을 수신하기 위해 필요한 버퍼의 크기입니다.

## 버전

> EmEditor 버전 7 이상에서만 지원됩니다.