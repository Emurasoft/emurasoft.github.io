# 최근 글꼴 명령

## 요약

최근 사용 글꼴을 선택합니다 (여러 항목).

## 설명

이 명령은 최근 사용한 글꼴의 목록을 나타내는 여러 항목을 포함하고 있습니다.
이 명령은 지정된 글꼴을 선택합니다.
최근 파일에 표시될 글꼴의 수는 **도구** 메뉴 아래 [**사용자 지정 대화 상자**](../../dlg/customize/index) 의 [**기록 탭**](../../dlg/customize/history/index) 안 **최근 글꼴 수** 텍스트 박스에서
설정할 수 있습니다. (**도구** \> **사용자 지정** \> **기록**).

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **보기** >
**글꼴** \> (**최근 글꼴**)
- 도구 모음: ![](../../images/fontpopup.gif) (화살표 위) \>
(**최근 글꼴**)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_MRU_FONT1 through ID_MRU_FONT1 + 63 (from 4736 through 4736 +
```
63)

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4736 + i); // i is an integer from 0 through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4736 + i   ' i is an integer from 0
through 63
```
