# GREP\_INFOA

[Editor\_FindInFilesA 인라인 함수](../macro/editor_findinfilesa),
[Editor\_ReplaceInFilesA 인라인 함수](../macro/editor_replaceinfilesa)
( [EE\_FIND\_IN\_FILESA \
메시지](../message/ee_find_in_filesa), [EE\_REPLACE\_IN\_FILESA \
메시지](../message/ee_replace_in_filesa))에 의해 사용됩니다.

typedef struct \_GREP\_INFOA {

UINT cbSize;

UINT nCP;

UINT nFlags;

LPCSTR pszFind;

LPCSTR pszReplace;

LPCSTR pszPath;

LPCSTR pszBackupPath;

LPCSTR pszFilesToIgnore;

} GREP\_INFOA;

## 필드

_cbSize_

(GREP\_INFOA)의 크기를 지정합니다.

_nCP_

파일이 열린 코드 페이지를 지정합니다.

|     |     |
| --- | --- |
| CODEPAGE\_ANSI | 일반 ANSI |
| CODEPAGE\_UNICODE | 유니코드 (little-endian) |
| CODEPAGE\_UNICODE\_BIGENDIAN | 유니코드 (big-endian) |
| CODEPAGE\_UTF8 | UTF-8 |
| CODEPAGE\_UTF7 | UTF-7 |
| CODEPAGE\_932 | Japanese Shift JIS |
| CODEPAGE\_JIS | Japanese JIS |
| CODEPAGE\_EUC | Japanese EUC |
| CODEPAGE\_AUTO\_SJIS\_JIS | Japanese Shift JIS 와 JIS로부터 변환. |
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | Japanese Shift JIS、JIS、EUC 로부터 변환. |
| Others | 시스템으로 사용 가능한 모든 코드 페이지. |
| CODEPAGE\_DETECT\_UNICODE | 유니코드를 검색합니다. 다른 값과 결합될 수 있습니다. |
| CODEPAGE\_DETECT\_UTF8 | UTF-8를 검색합니다. 다른 값과 결합될 수 있습니다. |
| CODEPAGE\_DETECT\_CHARSET | HTML/XML 문자 집합을 검색합니다. 다른 값과 결합될 수 있습니다. |
| CODEPAGE\_DETECT\_ALL | 모드 코드 페이지를 검색합니다. 다른 값과 결합될 수 있습니다. |

_nFlags_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 대,소문자를 일치시킵니다. |
| FLAG\_FIND\_ESCAPE | 이스케이프 시퀀스를 사용합니다. FLAG\_FIND\_REG\_EXP와 결합될 수 없습니다. |
| FLAG\_FIND\_ONLY\_WORD | 단어만을 검색합니다. |
| FLAG\_FIND\_REG\_EXP | 정규식 표현을 사용합니다. FLAG\_FIND\_ESCAPE와 결합될 수 없습니다. |
| FLAG\_FIND\_RECURSIVE | 지정된 경로의 하위 폴더를 검색합니다. |
| FLAG\_FIND\_FILENAMES\_ONLY | 파일 이름만 표시합니다. |
| FLAG\_REPLACE\_KEEP\_OPEN | 수정된 파일들을 연 상태로 유지합니다. eeReplaceBackup과 결합될 수 없습니다. FLAG\_REPLACE\_BACKUP과 <br> 결합될 수 없습니다. |
| FLAG\_REPLACE\_BACKUP | 백업을 저장합니다. FLAG\_REPLACE\_KEEP\_OPEN과 결합될 수 없습니다. |
| FLAG\_FIND\_IGNORE\_FILES | _pszFilesToIgnore_ 에 의해 지정된 파일이나 폴더를 무시합니다. |
| FLAG\_FIND\_OUTPUT | 검색 결과를 출력 표시줄로 재지정합니다. |

_pszFind_

검색할 문자열을 지정합니다.

_pszReplace_

파일 내 바꾸기를 할 때, 대체할 문자열을 지정합니다.

_pszPath_

검색할 경로를 지정합니다.
\*과 ?와 같은 와일드 카드를 포함할 수 있습니다.

_pszBackupPath_

_nFlags_ 가 FLAG\_REPLACE\_BACKUP을 포함하는 경우, 파일 내 바꾸기를 할 때 백업 폴더를 지정합니다.

_pszFilesToIgnore_

_nFlags_ 가 FLAG\_FIND\_IGNORE\_FILES를 포함하는 경우, 무시할 파일 또는 폴더의 이름을 지정합니다. \* 과 ?같은 와일드 카드를 포함할 수 있습니다.
다중 파일을 지정하려면, 구분하기 위해 세미콜론(;)을 사용합니다.

## 버전

EmEditor 버전 4.02 이상에서만 지원됩니다.
