# FindInFiles 메서드 (Editor ��ü)

일치하는 문자열을 위해 여러 파일을 검색합니다. 검색된 파일의 결과 목록은 현재 창에 표시됩니다.
문서가 저장되지 않은 경우, 이 메서드는 파일을 저장할지 여부를 확인하는 메시지를 나타냅니다.

#### \[JavaScript\]

editor. **FindInFiles**( _strFind_, _strPath_, _nFlags_, _nEncoding_, _strFilesToIgnore_  );

#### \[VBScript\]

editor. **FindInFiles** _strFind_, _strPath_, _nFlags_, _nEncoding_, _strFilesToIgnore_

## 매개 변수

_strFind_

검색할 문자열을 지정합니다.

_strPath_

검색하는 경로를 지정합니다. \\* 과 ?같은 와일드 카드를 포함할 수 있습니다.

_nFlags_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| eeFindFileNamesOnly | 파일 이름만 표시합니다. |
| eeFindOutput | 출력 표시줄에 검색 결과를 리디렉션합니다. |
| eeFindRecursive | 지정된 경로의 하위 폴더를 검색합니다. |
| eeFindReplaceCase | 대,소문자를 일치합니다. |
| eeFindReplaceEscSeq | 이스케이프 시퀀스를 사용합니다. eeFindReplaceRegExp과는 결합할 수 없습니다. |
| eeFindReplaceIgnoreFiles | _strFilesToIgnore_ 로 지정된 파일이나 폴더는 무시됩니다. |
| eeFindReplaceOnlyWord | 단어만 검색합니다. |
| eeFindReplaceRegExp | 정규 표현식을 사용합니다. eeFindReplaceEscSeq과는 결합할 수 없습니다. |
| eeFindSaveHistory | 반복 검색을 위한 검색된 문자열을 저장합니다. |
| eeOpenDetectAll | 모든 인코딩을 검색합니다. |
| eeOpenDetectCharset | HTML/XML 문자 집합을 검색합니다. |
| eeOpenDetectUnicode | 유니코드 서명(BOM)을 검색합니다. |
| eeOpenDetectUTF8 | UTF-8을 검색합니다. |

_nEncoding_

**[인코딩 상수](../const/const_encoding)** 에서 선택하거나 Windows 운영 체제에서 사용되는 코드 페이지를 지정합니다.

_strFilesToIgnore_

_nFlags_ 가 eeFindReplaceIgnoreFiles을 포함하는 경우,
무시하려는 파일이나 폴더 이름을 지정합니다. \\* 과 ?같은 와일드 카드를 포함할 수 있습니다.
여러 파일들을 지정하려면 구분하기 위해 세미콜론(;)을 사용합니다.

## 버전

엠에디터 프로페셔널 버전 4.02 이상에서만 지원됩니다.