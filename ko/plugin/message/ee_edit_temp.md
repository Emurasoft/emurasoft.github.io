# EE\_EDIT\_TEMP

새로운 문서를 임시 텍스트로 열거나, 기존의 임시 텍스트를 활성화, 저장, 또는 닫습니다.

이 메시지를 명시적으로 또는 [Editor\_ActivateTemp](../macro/editor_activatetemp), [Editor\_CloseTemp](../macro/editor_closetemp),
[Editor\_EditTemp](../macro/editor_edittemp), 및 [Editor\_SaveTemp](../macro/editor_savetemp) 인라인 함수를
사용하여 보낼 수 있습니다.

EE\_EDIT\_TEMP

wParam = 0;

lParam = (LPARAM) (TEMP\_INFO) pTI;

## 매개 변수

_pTI_

> [TEMP\_INFO](../structure/temp_info) 구조에 대한 포인터 입니다.

## 반환 값

> 반환 값은 새로운 문서의 ID입니다. 하지만, 임시 텍스트를 닫으면 사용되지 않습니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.