# OpenFile 메서드 (Editor ��ü)

기존 파일을 엽니다.

#### \[JavaScript\]

editor. **OpenFile**( _strFileName_, _nEncoding_, _nFlags_
);

#### \[VBScript\]

editor. **OpenFile** _strFileName_, _nEncoding_, _nFlags_

## 매개 변수

_strFileName_

열 파일의 이름과 전체 경로를 지정합니다.

_nEncoding_

**[인코딩 상수](../const/const_encoding)** 에서 선택하거나,
Windows 운영 체제에서 사용되는 인코딩을 지정합니다.
0이 지정되거나 생략되면, 이 메서드는 속성에 의해 미리 정의된 인코딩으로 파일을 엽니다.

_nFlags_

다음의 값들의 결합을 지정합니다.
nEncoding이 0 이거나 생략된 경우, eeOpenAllowNewWindow를 제외한 모든 값은 무시됩니다.

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | 현재 문서에 제목이 지정되었거나 수정된 경우 새로운 창으로 엽니다. |
| eeOpenDetectUnicode | 유니코드 서명(BOM)을 검색합니다. |
| eeOpenDetectUTF8 | UTF-8를 검색합니다. |
| eeOpenDetectCharset | HTML/XML 문자 집합을 검색합니다. |
| eeOpenDetectAll | 모든 인코딩을 검색합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
하지만, nEncoding 과 nFlags 매개 변수는 버전 5.00 이상에서 삭제될 수 있습니다.