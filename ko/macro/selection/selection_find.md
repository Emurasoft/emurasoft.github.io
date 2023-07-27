# Find 메서드 (Selection ��ü)

지정된 문자열을 검색합니다.

## 

### \[JavaScript\]

```
nFound = document.selection.Find( strFind, nFlags );
```

### \[VBScript\]

```
nFound = document.selection.Find( strFind, nFlags )
```

## 매개 변수

_strFind_

검색할 문자열을 지정합니다.

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeFindAround | 문서의 끝에 도달하였을 때 문서의 시작점으로 이동합니다. |
| eeFindBookmark | 문자열이 일치하는 줄에 책갈피를 설정합니다. |
| eeFindCount | 일치하는 문자열의 발생 횟수를 셉니다. |
| eeFindNext | 커서 위치에서 아래로 검색합니다. |
| eeFindPrevious | 커서 위치에서 위로 검색합니다. |
| eeFindReplaceCase | 대,소문자를 일치시킵니다. |
| eeFindReplaceEscSeq | 이스케이프 시퀀스를 사용합니다. eeFindReplaceRegExp와 결합될 수 없습니다. |
| eeFindReplaceOnlyWord | 전체 단어만 일치합니다. |
| eeFindReplaceOpenDoc | 동일한 프레임 안 모든 열린 문서들을 검색합니다. |
| eeFindReplaceQuiet | 아무런 문자열도 발견되지 않은 경우 상태 표시줄에 메시지를 나타내지 않습니다. |
| eeFindReplaceRegExp | 검색 문자열에 정규식 표현을 사용합니다. eeFindReplaceEscSeq과 결합될 수 없습니다. |
| eeFindSaveHistory | 반복 검색을 위해 검색할 문자열을 저장합니다. |
| eeFindSelectAll | 모든 일치하는 문자열을 선택합니다. |

## 반환 값

검색한 문자열이 발견된 경우 1로 반환하거나 발견되지 않는 경우 0을 반환합니다.
하지만, eeFindCount 플래그가 지정되면 반환 값은 문서 내 일치하는 문자열의 발생 횟수가 됩니다.
그렇지만, 커서 위치에서 지정한 방향으로 검색한 문자열이 발견되지 않으면
문서의 나머지 부분에서 일치하는 문자열이 발견되더라도
반환 값이 0이 됩니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
