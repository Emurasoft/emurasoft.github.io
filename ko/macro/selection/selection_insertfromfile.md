# InsertFromFile 메서드 (Selection ��ü)

커서 위치에 지정된 파일의 내용을 삽입합니다.

#### \[JavaScript\]

document.selection. **InsertFromFile**( _strFileName_, _nEncoding_, _nFlags_ );

#### \[VBScript\]

document.selection. **InsertFromFile** _strFileName_, _nEncoding_, _nFlags_

_strFileName_

열 파일의 이름과 전체 경로를 지정합니다.

_nEncoding_

**[인코딩 상수](../const/const_encoding)** 에서 선택하거나 Windows 운영 체제에서 사용되는 코드 페이지를 지정합니다.

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | 현재 문서에 제목이 정해졌거나 수정된 경우에는 새로운 창에서 엽니다. |
| eeOpenDetectUnicode | 유니코드 서명(BOM)을 검색합니다. |
| eeOpenDetectUTF8 | UTF-8를 검색합니다. |
| eeOpenDetectCharset | HTML/XML 문자 집합을 검색합니다. |
| eeOpenDetectAll | 모든 인코딩을 검색합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.