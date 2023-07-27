# QueryStringByID 메서드 (Editor ��ü)

지정된 명령과 연관된 문자열을 검색합니다.

## 

### \[JavaScript\]

```
str = editor.QueryStringByID( nID );
```

### \[VBScript\]

```
str = editor.QueryStringByID( nID )
```

## 매개 변수

_nID_

실행할 명령 ID를 나타내는 정수를 지정합니다. 다음의 명령만을 사용할 수 있습니다.
자세한 내용은[명령 참조](../../cmd/index) 를 참고하십시오.

|     |     |     |
| --- | --- | --- |
| nID | 명령 이름 | 반환 값 |
| 4609 부터 4609 + 63 | [최근 파일 리스트](../../cmd/file/file_mru_file1) | 파일 경로와 이름 |
| 4864 부터 4864 + 63 | [최근 파일 삽입 리스트](../../cmd/file/file_mru_insert1) | 파일 경로와 이름 |
| 4992 부터 4992 + 63 | [최근 폴더 리스트](../../cmd/file/file_mru_folder1) | 파일 경로와 이름 |
| 5376 부터 5376 + 255 |[문서 목록](../../cmd/window/window_menu) | 창 제목 |
| 5632 부터 5632 + 255 |[플러그 인 목록](../../cmd/tools/plug_in1) | 플러그인 파일 이름 |
| 6656 부터 6656 + 255 | [다시로드할 인코딩 리스트](../../cmd/file/file_reload_defined) | 인코딩 이름 |
| 7680 부터 7680 + 255 | [인코딩하여 저장하기 리스트](../../cmd/file/file_save_defined) | 인코딩 이름 |
| 9216 부터 9216 + 1023 |[매크로 리스트](../../cmd/macros/macro1) | 매크로 경로와 이름 |

## 반환 값

nID 매개 변수에 따라 문자열의 어떤 의미인지 반환합니다.
nID 매개 변수가 유효하지 않은 경우, 그 메서드는 빈 문자열을 반환합니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
