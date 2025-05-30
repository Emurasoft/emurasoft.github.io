# 새로 만들기 (팝업 메뉴) 명령

## 요약

지정된 구성을 사용하여 새로운 파일을 생성하는 팝업 메뉴를 표시합니다.

## 설명

이 명령은 엠에디터의 새로운 창을 나타내고 새로운 문서 작성을 시작할 준비를 합니다. 이 명령은 디스크에 파일을 즉각적으로 생성하지 않습니다.
문서를 작정하고 [**저장** 명령](file_save) 또는 [**다른 이름으로 저장** 명령](file_save_as) 을 선택할 때 까지 파일은 생성되지 않습니다.

이 명령은 팝업 메뉴를 나타내고 (텍스트, HTML, VBScript과 같은)시작할 구성을 선택할수 있게 합니다. 만약 지정된 구성이 템플릿 파일로 구성된 경우, 그 템플릿이 시작 문서로 사용됩니다.
[**현재 구성 속성** 버튼](../tools/customize) (또는 ALT + ENTER)을 클릭하고 [**파일 탭**](../../dlg/properties/file/index) 을 선택한 후 **새 파일**
버튼을 눌러 [**새 파일 상세 정보** 대화 상자](../../dlg/properties/file/new_details/index) 에서
템플릿 파일, 새로운 파일의 인코딩, 변환 방법 및 글꼴 범주를 설정할 수 있습니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **새로 만들기** \> **새로 만들기 (팝업 메뉴)**
- 도구 모음: ![](../../images/filenew.png)
(화살표 위)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_NEW_CONFIG_POPUP (4281)
```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4281);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4281
```
