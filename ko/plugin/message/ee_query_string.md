# EE\_QUERY\_STRING

지정된 명령과 관련된 문자열을 검색합니다. 이 메시지를 명시적으로 또는
[Editor\_QueryString](../macro/editor_querystring) 인라인 함수를 사용하여 보낼 수 있습니다.

```
EE_QUERY_STRING
wParam = (WPARAM) MAKEWPARAM( nCmdID, bShortTitle );
lParam = (LPARAM) (LPWSTR) psz;
```

## 매개 변수

_nCmdID_

실행할 명령 ID를 나타내는 정수를 지정합니다. 다음의 명령만 사용될 수 있습니다.
더 자세한 정보를 위해 **[Command Reference](../../cmd/index)** 을 참조하시기 바랍니다.

|     |     |     |
| --- | --- | --- |
| nID | 명령 이름 | 반환 값 |
| 4609 through 4609 + 63 | [**최근 파일 리스트 명령**](../../cmd/file/file_mru_file1) | 파일 경로와 이름 |
| 4864 through 4864 + 63 | [**최근 파일 삽입 리스트 명령**](../../cmd/file/file_mru_insert1) | 파일 경로와 이름 |
| 4992 through 4992 + 63 | [**최근 폴더 리스트 명령**](../../cmd/file/file_mru_folder1) | 파일 경로와 이름 |
| 5376 through 5376 + 255 | **[문서 목록 명령](../../cmd/window/window_menu)** | 창 제목 |
| 5632 through 5632 + 255 | **[플러그 인 목록 명령](../../cmd/tools/plug_in1)** | 플러그 인 파일 이름 |
| 6656 through 6656 + 255 | [**다시로드할 인코딩 리스트 명령**](../../cmd/file/file_reload_defined) | 인코딩 이름 |
| 7680 through 7680 + 255 | [**인코딩하여 저장하기 리스트 명령**](../../cmd/file/file_save_defined) | 인코딩 이름 |
| 9216 through 9216 + 1023 | **[매크로 리스트 명령](../../cmd/macros/macro1)** | 매크로 경로와 이름 |

_bShortTitle_

특정한 명령에 짧은 버전의 문자열이 필요한 지 여부를 지정합니다.

_psz_

문자열을 검색하기 위해 버퍼를 지정합니다.

## 반환 값

command ID가 유효한 경우, 반환 값은 0 이 아닙니다. 그렇지 않으면, 반환 값은 0입니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
