# 최근 파일 리스트 명령

## 요약

최근 엑세스 한 지정된 문서를 엽니다 (여러 항목).

## 설명

이 명령은 최근 엑세스한 파일들의 리스트를 나타내는 여러 메뉴 항목을 포함하고 있습니다.
이 명령은 지정된 파일을 엽니다. **도구** 메뉴 아래 [**사용자 지정 대화 상자**](../../dlg/customize/index) 의 [**기록 탭**](../../dlg/customize/history/index) 의 **최근 파일 수** 텍스트 박스에서 최근 파일로 나타낼 파일의 수를 설정 할 수 있습니다. **(도구** \> **사용자 지정** \> **기록**)

## 실행하는 방법

- 기본 메뉴: **파일** > **(파일 이름 선택)**
- [모든 명령](../tools/all_commands): **파일** \> **열기**
\> **최근 파일** \> **(파일 이름 선택)**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_FILE_MRU_FILE1 through EEID_FILE_MRU_FILE1 + 63 (from 4609```
through 4609 + 63)

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID (4609 + i);  // i is an integer from 0
through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4609 + i  ' i is an integer from 0 through
63
```
