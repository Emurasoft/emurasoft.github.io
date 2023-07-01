# Editor\_DocInfo

EmEditor에 사용되는 정보 매개 변수 중 하나의 값을 검색하거나 설정합니다. 이 인라인 함수를 사용하거나
[EE\_INFO](../message/ee_info) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_DocInfo( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## 매개 변수

_nCmd_

> 검색하거나 설정할 매개 변수를 지정합니다.
> 이 매개 변수는 다음 테이블 값들 중 하나가 될 수 있습니다.
>
> |     |     |     |     |
> | --- | --- | --- | --- |
> | **nCmd** | **의미** | **lParam** | **Return 값** |
> | EI\_GET\_ENCODE | 파일을 저장할 인코딩 방법을 검색합니다. | 사용되지 않습니다. | (int)nCP<br> 인코딩 방법. |
> | EI\_SET\_ENCODE | 파일을 저장할 인코딩 방법을 설정합니다. | (UINT)nCP<br> 값이 CODEPAGE\_로 시작하는 인코딩 방법을 지정합니다. | 사용되지 않습니다. |
> | EI\_GET\_SIGNATURE | 서명 유니코드/UTF-8 파일인지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bSignature<br> 서명에 TRUE |
> | EI\_SET\_SIGNATURE | 서명 유니코드/UTF-8 파일인지 여부를 설정합니다. | (BOOL)bSignature<br> 서명에 TRUE | 사용되지 않습니다. |
> | EI\_GET\_FONT\_CHARSET | 표시할 문자 집합을 검색합니다. | 사용되지 않습니다. | (int)nCharset<br> 문자 집합. |
> | EI\_SET\_FONT\_CHARSET | 표시할 문자 집합을 설정합니다. | (int)nCharset<br> 값이 CHARSET\_로 시작하는 문자 집합을 지정합니다. | 사용되지 않습니다. |
> | EI\_GET\_FONT\_CP | 표시할 글꼴이 사용된 코드 페이지를 검색합니다. | 사용되지 않습니다. | (UINT)nCP<br> 코드 페이지. |
> | EI\_GET\_INPUT\_CP | 입력 언어가 사용된 코드 페이지를 검색합니다. | 사용되지 않습니다. | (UINT)nCP<br> 코드 페이지. |
> | EI\_GET\_SHOW\_TAG | 강조 표시된 태그를 보일지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bShowTag<br> 태그 강조에 TRUE |
> | EI\_SET\_SHOW\_TAG | 강조 표시된 태그를 보일지 여부를 설정합니다. | (BOOL)bShowTag<br> 태그 강조에 TRUE | 사용되지 않습니다. |
> | EI\_GET\_FILE\_NAMEA | 현재 열려있는 파일 이름을 바이트로 검색합니다. | (LPSTR)szFileName<br> 파일 이름을 검색할 버퍼에 포인터를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_FILE\_NAMEW | 현재 열려있는 파일 이름을 유니코드로 검색합니다. | (LPSTR)szFileName<br> 파일 이름을 검색할 버퍼에 포인터를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_IS\_PROPORTIONAL\_FONT | 표시 글꼴이 비례하는지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bProportionalFont |
> | EI\_GET\_NEXT\_BOOKMARK | 다음 책갈피 위치를 검색합니다. | (int)yLine<br> 검색 할 초기 논리 줄을 지정합니다. -1은 문서의 시작으로부터 검색을 합니다. | (int)yLine<br> 검색된 논리 줄을 반환합니다. 찾지 못한 경우 -1이 반환됩니다. |
> | EI\_GET\_HILITE\_FIND | 검색된 문자열을 강조 표시할지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bShowFindHilite |
> | EI\_SET\_HILITE\_FIND | 검색된 문자열을 강조 표시할지 여부를 설정합니다. | (BOOL)bShowFindHilite | 사용되지 않습니다. |
> | EI\_GET\_APP\_VERSIONA | 버전 이름을 ANSI 문자열로 검색합니다. | (LPSTR)szVersionName<br> 버전 문자열을 검색할 버퍼에 포인터를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_APP\_VERSIONW | 버전 이름을 유니코드 문자열로 검색합니다. | (LPWSTR)szVersionName<br> 버전 문자열을 검색할 버퍼에 포인터를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_READ\_ONLY | 문서가 읽기 전용인지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bReadOnly |
> | EI\_IS\_WINDOW\_COMBINED | 창이 결합되었는지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bCombined |
> | EI\_WINDOW\_COMBINE | 창이 결합되었는지 여부를 설정합니다. | (BOOL)bCombined<br> TRUE인 경우 창을 결합하고, FALSE인 경우 창을 구분합니다. | 사용되지 않습니다. |
> | EI\_IS\_UNDO\_COMBINED | 삽입된 문자열이 한번에 실행 취소 될수 있는지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bCombined |
> | EI\_GET\_DOC\_COUNT | 현재 프레임 창에 열려있는 문서의 수를 검색합니다.(EmEditor 버전 5 이상에서만 지원됩니다.). | 사용되지 않습니다. | (int)nCount<br> 문서의 수를 반환합니다. |
> | EI\_INDEX\_TO\_DOC | 문서 인덱스를 문서 핸들로 변환합니다.(EmEditor 버전 5 이상에서만 지원됩니다.). | 문서의 0으로 시작하는 인덱스를 지정합니다. | (HEEDOC)hDoc<br> 문서에 대한 핸들을 반환합니다. |
> | EI\_DOC\_TO\_INDEX | 문서 핸들을 문서 인덱스로 변환합니다. | 문서에 핸들을 지정합니다. | (int)nIndex<br> 문서의 0으로 시작하는 인덱스를 반환합니다. |
> | EI\_ZORDER\_TO\_DOC | 문서 z-순서를 문서 핸들로 변환합니다. | 문서의 0으로 시작하는 z-순서를 지정합니다. | (HEEDOC)hDoc<br> 문서에 대한 핸들을 반환합니다. |
> | EI\_DOC\_TO\_ZORDER | 문서 핸들을 문서 z-순서로 변환합니다. | 문서에 핸들을 지정합니다. | (int)nZOrder<br> 문서의 0으로 시작하는 z-순서를 반환합니다. |
> | EI\_GET\_ACTIVE\_INDEX | 활성화 문서의 인덱스를 검색합니다. | 사용되지 않습니다. | (int)nIndex<br> 문서의 0으로 시작하는 인덱스를 반환합니다. |
> | EI\_SET\_ACTIVE\_INDEX | 문서를 활성화합니다. | 사용되지 않습니다. | (BOOL)bSuccess<br> 성공하면 TRUE를 실패하는 경우 FALSE를 반환합니다. |
> | EI\_GET\_FULL\_TITLEA | ANSI 문자열 내 문서의 전체 제목을 검색합니다. | (LPSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_FULL\_TITLEW | 유니코드 문자열 내 문서의 전체 제목을 검색합니다. | (LPWSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_SHORT\_TITLEA | ANSI 문자열 내 문서의 짧은 제목을 검색합니다. | (LPSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_SHORT\_TITLEW | 유니코드 문자열 내 문서의 짧은 제목을 검색합니다. | (LPWSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_SAVE\_AS\_TITLEA | ANSI 문자열내 수정을 나타내는 별표(\*)를 제외한 문서의 전체 제목을 검색합니다. | (LPSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_GET\_SAVE\_AS\_TITLEW | 유니코드 문자열 내 수정을 나타내는 별표(\*)를 제외한 문서의 전체 제목을 검색합니다. | (LPWSTR)szTitle<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_MOVE\_ORDER | 문서 탭 순서를 이동합니다. | 대상 탭의 0으로 시작하는 인덱스를 지정합니다. | 사용되지 않습니다. |
> | EI\_CLOSE\_DOC | 문서를 닫습니다. | 사용되지 않습니다. | (BOOL)bSuccess<br> 성공하면 TRUE를 실패하는 경우 FALSE를 반환합니다. |
> | EI\_SAVE\_DOC | 문서를 저장합니다. 문서의 제목이 정해지지 않은 경우 **다른 이름으로 저장** 대화 상자가 나타납니다. | 사용되지 않습니다. | (BOOL)bSuccess<br> 성공하면 TRUE를 실패하는 경우 FALSE를 반환합니다.문서에 이름이 지정되지 않았을 때 **다른 이름으로 저장** 대화 상자에서 취소를 누르면 FALSE가 반환됩니다. |
> | EI\_GET\_CURRENT\_FOLDER | 현재 작업중인 폴더를 검색합니다. | (LPWSTR)szDir<br> 문자열을 검색하기 위해 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | 사용되지 않습니다. |
> | EI\_IS\_LARGE\_DOC | 문서가 매우 큰지 여부를 나타내는 flag를 검색합니다. | 사용되지 않습니다. | (BOOL)bLarge<br> 문서가 매우 큰 경우 TRUE를 반환합니다. 그렇지 않으면 FALSE를 반환합니다. |
> | EI\_USE\_INI | 레지스트리 대신에 INI 파일이 사용되었는지 여부를 검색합니다. | 사용되지 않습니다. | (BOOL)bIni<br> INI 파일이 사용되면 TRUE를, 레지스트리가 사용되면 FALSE를 반환합니다. |
> | EI\_GET\_LANGUAGE | 사용자 인터페이스에 현재 선택된 언어를 검색합니다. | (LPWSTR)szFolder<br> 언어 폴더를 검색할 버퍼를 지정합니다.버퍼는 종료된 NULL문자를 포함하는 MAX\_PATH 단어만큼이어야 합니다. | (UINT)nLangID<br> 현재 선택된 언어 ID를 반환합니다. |
> | EI\_COMBINE\_HISTORY | 실행 취소에 대한 한 기록으로 이전 변경에 다음 변경을 결합 할지 여부를 지정합니다. | (BOOL)bCombine<br> 결합에 TRUE | 사용되지 않습니다. |
> | EI\_GET\_BAR\_TEXT\_COLOR | 사용자 지정 표시줄의 텍스트 색상을 검색합니다. | 사용되지 않습니다. | (COLORREF)clrText<br> 텍스트 색상의 RGB값을 반환합니다. |
> | EI\_GET\_BAR\_BACK\_COLOR | 사용자 지정 표시줄의 배경 색상을 검색합니다. | 사용되지 않습니다. | (COLORREF)clrBack<br> 배경 색상의 RGB 값을 반환합니다. |
> | EI\_GET\_RETURN\_TYPE | 현재 줄의 반환 유형을 검색합니다. 현재 줄이 문서의 마지막 줄이고 반환을 가지고 있지 않은 경우, 이전 줄의 반환 유형을 검색합니다. | (UINT\_PTR)yLogicalLine<br> 논리 줄의 인덱스를 지정합니다. | (int)nReturnType<br> RETURN\_METHOD\_BOTH, RETURN\_METHOD\_CR\_ONLY, 또는 RETURN\_METHOD\_LF\_ONLY를 반환합니다. |
> | EI\_GET\_ACTIVE\_DOC | 활성화 문서에 핸들을 검색합니다. | 사용되지 않습니다. | (HEEDOC)hDoc<br> 문서에 대한 핸들을 반환합니다. |
> | EI\_SET\_ACTIVE\_DOC | 문서를 활성화합니다. | (HEEDOC)hDoc<br>활성화된 문서에 핸들을 지정합니다. | (BOOL)bSuccess<br> 성공하면 TRUE를 실패하는 경우 FALSE를 반환합니다. |
> | EI\_GET\_SYNC\_SESSION | 문서가 비교중이거나 동기화 스크롤 모드인 경우 session ID를 검색합니다. | 사용되지 않습니다. | (int)nSessionID<br> 문서가 비교중이거나 동기화 스크롤 모드인 경우 session ID를 반환합니다. 문서가 일반 모드 인 경우 0이 반환됩니다. |
> | EI\_GET\_LOC\_DLL\_INSTANCE | 지역화 된 리소스 DLL의 인스턴스 핸들을 검색합니다. | 사용되지 않습니다. | (HINSTANCE)hinstLoc<br> 지역화 된 리소스 DLL의 인스턴스 핸들을 반환합니다. |
> | EI\_GET\_RES\_DLL\_INSTANCE | 리소스 DLL의 인스턴스 핸들을 검색합니다. | 사용되지 않습니다. | (HINSTANCE)hinstRes<br> 리소스 DLL의 인스턴스 핸들을 반환합니다.. |
> | EI\_GET\_CMD\_LIST\_SIZE | 지정된 다중-메뉴 명령에 사용 가능한 항목의 수를 검색합니다. | 다중-메뉴 comman ID의 첫번째 항목입니다. | (int)nCount<br>사용 가능한 항목의 수를 반환합니다. |

_iDoc_

> 대상 문서의 0으로 시작하는 인덱스를 지정합니다. -1이 지정된 경우, 현재 활성화 중인 문서가 대상으로 지정됩니다.

_lParam_

> 지정된 매개 변수에 의해 결정됩니다.

## 반환 값

> 지정된 매개 변수에 의해 결정됩니다.

## 버전

> 엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
