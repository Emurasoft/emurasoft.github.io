# Replace 메서드 (Selection ��ü)

문서 내 문자열을 대체합니다.

## 

### \[JavaScript\]

```
nFound = document.selection.Replace( strFind, strReplace,
nFlags );
```

### \[VBScript\]

```
nFound = document.selection.Replace( strFind, strReplace,
nFlags )
```

## 매개 변수

_strFind_

검색할 문자열을 지정합니다.

_strReplace_

대체할 문자열을 지정합니다.

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeFindReplaceCase | 대,소문자를 일치시킵니다. |
| eeFindReplaceEscSeq | 이스케이프 시퀀스를 사용합니다. eeFindReplaceRegExp과 결합할 수 없습니다. |
| eeFindReplaceOnlyWord | 전체 단어만 일치합니다. |
| eeFindReplaceOpenDoc | 동일한 프레임 창 내에 열린 모든 문서를 검색합니다. |
| eeFindReplaceQuiet | 아무런 문자열을 발견하지 못하면 상태 표시줄에 메시지를 표시하지 않습니다. |
| eeFindReplaceRegExp | 검색할 문자열에 정규식 표현을 사용합니다. eeFindReplaceEscSeq과 결합할 수 없습니다. |
| eeFindSaveHistory | 반복 검색을 위해 검색할 문자열을 저장합니다. |
| eeReplaceAll | 한 번에 모두 대체합니다. |
| eeReplaceSelOnly | 선택 영역 안에서만 대체합니다. |

## 반환 값

eeReplaceAll이 지정되면 대체된 문자열의 수를 반환합니다.
그렇지 않으면, 발견하는 경우 1을 반환하거나 발견하지 못한 경우 0을 반환합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
