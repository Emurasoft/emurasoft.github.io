# LOAD\_FILE\_INFO\_EX

[Editor\_LoadFileA](../macro/editor_loadfilea) 와
[Editor\_LoadFileW](../macro/editor_loadfilew)
인라인 함수 ( [EE\_LOAD\_FILEA](../message/ee_load_filea) 와
[EE\_LOAD\_FILEW](../message/ee_load_filew) 메시지)에 의해 사용됩니다.

typedef struct \_LOAD\_FILE\_INFO\_EX {

UINT cbSize;

UINT nCP;

BOOL bDetectUnicode;

BOOL bDetectAll;

BOOL bDetectCharset;

BOOL bDetectUTF8;

UINT nFlags;

} LOAD\_FILE\_INFO\_EX;

## 필드

_cbSize_

> sizeof(LOAD\_FILE\_INFO\_EX)이어야만 합니다.

_nCP_

> 파일이 열린 코드 페이지를 지정합니다.
>
> |     |     |
> | --- | --- |
> | CODEPAGE\_ANSI | 일반 ANSI |
> | CODEPAGE\_UNICODE | 유니코드 (little-endian) |
> | CODEPAGE\_UNICODE\_BIGENDIAN | 유니코드 (big-endian) |
> | CODEPAGE\_UTF8 | UTF-8 |
> | CODEPAGE\_UTF7 | UTF-7 |
> | CODEPAGE\_932 | Japanese Shift JIS |
> | CODEPAGE\_JIS | Japanese JIS |
> | CODEPAGE\_EUC | Japanese EUC |
> | CODEPAGE\_AUTO\_SJIS\_JIS | Japanese Shift JIS 와 JIS로부터 변환. |
> | CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | Japanese Shift JIS、JIS、EUC 로부터 변환. |
> | Others | 시스템으로 사용 가능한 모든 코드 페이지. |

_bDetectUnicode_

> TRUE인 경우, 유니코드가 검색됩니다.

_bDetectAll_

> TRUE인 경우, 모든 코드 페이지가 검색됩니다.

_bDetectCharset_

> TRUE인 경우, HTML/XML 문자 조합이 검색됩니다.

_bDetectUTF8_

> TRUE인 경우, UTF-8이 검색됩니다.

_nFlags_

> 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | LFI\_ALLOW\_ASYNC\_OPEN | 비동기적으로 파일을 열도록 합니다. |
> | LFI\_ALLOW\_NEW\_WINDOW | 새로운 창에 파일을 엽니다. |
