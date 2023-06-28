# setData 메서드

클립보드에 지정된 형식 내 데이터를 할당합니다.

#### \[JavaScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData_, _iPos_ );

#### \[VBScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData, iPos_ )

## 매개 변수

_sDataFormat_

다음 데이터 형식 값을 하나 이상 지정하는 문자열입니다.

|     |     |
| --- | --- |
| Text | 텍스트를 포함한 모든 형식을 삭제합니다. |
| LineText | 줄 텍스트 형식을 삭제합니다. |
| BoxText | 박스 텍스트 형식을 삭제합니다. |

_sData_

문자열로 텍스트 데이터를 지정합니다.

_iPos_

선택 사항입니다. 이전의 클립보드 데이터를 설정하고 싶은 경우에는 클립보드 기록 내 위치를 지정합니다.
0 이거나 생략된 경우에는, 현재 데이터가 할당됩니다.

## 예시

#### \[JavaScript\]

clipboardData.setData("Text", "Hello!");

#### \[VBScript\]

clipboardData.setData "Text", "Hello!"

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.