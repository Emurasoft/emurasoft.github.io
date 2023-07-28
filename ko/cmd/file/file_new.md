# 새 텍스트 명령

## 요약

새 텍스트 파일을 생성합니다.

## 설명

이 명령은 엠에디터의 새로운 창을 나타내고 새로운 문서 작성을 시작할 준비를 합니다. 이 명령은 디스크에 파일을 즉각적으로 생성하지 않습니다.
문서를 작정하고 [**저장** 명령](file_save) 또는 [**다른 이름으로 저장** \
명령](file_save_as) 을 선택할 때 까지 파일은 생성되지 않습니다.

이 명령은 기본적으로 텍스트 구성을 사용합니다. [**구성 정의** 대화 상자](../../dlg/configurations/index) 에서
기본 구성을 변경 할 수 있습니다. 텍스트 구성은 기본적으로 [시스템 기본 인코딩](../../glossary/index) 를 쓰며, 반환 방법으로는 CR+LF  (Windows)를 사용하고,
영어 버전의 윈도우에서는 글꼴 범주로 서부 유럽체를 사용하며, 템플렛을 사용하지 않습니다.
[**현재 구성 속성** \
버튼](../tools/customize) (또는 ALT + ENTER)을 클릭하고 [**파일 탭**](../../dlg/properties/file/index) 을 선택한 후 **새 파일**
버튼을 눌러 [**새 파일 상세 정보** 대화 상자](../../dlg/properties/file/new_details/index) 에서
기본 설정을 변경 할 수 있습니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **새로 만들기** \> **새 텍스트**
- 도구 모음: ![](../../images/filenew.gif) (화살표
위 아님)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+N

## 플러그인 명령 ID

```
EEID_FILE_NEW (4096)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4096);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4096
```
