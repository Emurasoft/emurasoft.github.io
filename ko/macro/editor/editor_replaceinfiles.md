# ReplaceInFiles 메서드 (Editor ��ü)

여러 파일 내에서 텍스트를 대체합니다.

#### \[JavaScript\]

editor. **ReplaceInFiles**( _strFind_, _strReplace_, _strPath_, _nFlags_, _nEncoding_, _strFilesToIgnore_, _strBackupPath_ );

#### \[VBScript\]

editor. **ReplaceInFiles** _strFind_, _strReplace_, _strPath_, _nFlags_, _nEncoding_, _strFilesToIgnore_, _strBackupPath_

## 매개 변수

_strFind_

검색할 문자열을 지정합니다.

_strReplace_

대체할 문자열을 지정합니다.

_strPath_

검색할 경로를 지정합니다. \\* 과 ?같은 와일드 카드를 포함할 수 있습니다.

_nFlags_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| eeFindRecursive | 지정된 경로의 하위 폴더를 검색합니다. |
| eeFindReplaceCase | 대,소문자를 일치시킵니다. |
| eeFindReplaceEscSeq | 이스케이프 시퀀스를 사용합니다. eeFindReplaceRegExp와 함께 결합할 수 없습니다. |
| eeFindReplaceIgnoreFiles | _strFilesToIgnore_ 에 의해 지정된 폴더나 파일을 무시합니다. |
| eeFindReplaceOnlyWord | 단어만을 검색합니다. |
| eeFindReplaceRegExp | 정규식 표현을 사용합니다. eeFindReplaceEscSeq와 함께 결합할 수 없습니다. |
| eeFindSaveHistory | 반복 검색을 위해 검색할 문자열을 저장합니다. |
| eeOpenDetectAll | 모든 인코딩을 검색합니다. |
| eeOpenDetectCharset | HTML/XML 문자 집합을 검색합니다. |
| eeOpenDetectUnicode | 유니코드 서명(BOM)을 검색합니다. |
| eeOpenDetectUTF8 | UTF-8를 검색합니다. |
| eeReplaceBackup | 백업을 저장합니다. eeReplaceKeepOpen과 함께 결합할 수 없습니다. |
| eeReplaceKeepOpen | 수정된 파일들을 연 상태로 유지합니다. eeReplaceBackup과 함께 결합할 수 없습니다. |

_nEncoding_

**[인코딩 상수](../const/const_encoding)** 에서 선택하거나 Windows 운영 체제에서 사용되는 코드 페이지를 지정합니다.

_strFilesToIgnore_

_nFlags_ 가 eeFindReplaceIgnoreFiles을 포함한 경우
무시할 파일이나 폴더의 이름을 지정합니다. \\* 과 ?같은 와일드 카드를 포함할 수 있습니다.
여러 파일을 지정하려면 구분하기위해서 세미콜론(;)을 사용합니다.

_strBackupPath_

_nFlags_ 가 eeReplaceBackup을 지정하는 경우 백업 폴더를 정합니다.

## 주의

_nFlags_ 가 eeReplaceKeepOpen을 지정하지 않는한 이 작업은 취소될 수 없습니다.
_nFlags_ 로 eeReplaceBackup을 지정하고 백업을 저장하는 것을 권장합니다.
백업 폴더에 같은 파일 이름이 존재하는 경우, 새로운 백업이 오래된 이전 파일을 덮어씁니다.

## 버전

엠에디터 프로페셔널 버전 4.02 이상에서만 지원됩니다.
