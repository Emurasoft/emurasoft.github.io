# ChangeWidth 메서드 (Selection ��ü)

선택된 텍스트의 너비를 변경합니다.

#### \[JavaScript\]

document.selection. **ChangeWidth**( nFlags );

#### \[VBScript\]

document.selection. **ChangeWidth** nFlags

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다: eeWidthFullWidth 와 eeWidthHalfWidth를 함께 결합할 수 없습니다.

|     |     |
| --- | --- |
| eeWidthFullWidth | 반각 문자를 전각 문자로 변환합니다. |
| eeWidthHalfWidth | 전각 문자를 반각 문자로 변환합니다. |
| eeWidthKatakana | 가타카나로 변환을 적용합니다. |
| eeWidthAlphanumeric | 알파벳과 숫자로 변환을 적용합니다. |
| eeWidthMarks | 마크로 변환을 적용합니다. |
| eeWidthSpaces | 공백으로 변환을 적용합니다. |
| eeWidthKanaMarks | 가나 부호로 변환을 적용합니다. |
| eeWidthAllTypes | 모든 해당 가능한 문자로 변환을 적용합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.