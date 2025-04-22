# 다시로드할 인코딩 리스트 명령

## 요약

지정된 인코딩을 사용하여 현재 파일을 다시로드 합니다 (여러 항목).

## 설명

이 명령은 여러 메뉴 항목으로 구성되어 있으며 사전 정의된 인코딩을 선택할 수 있습니다.
이 명령은 지정된 인코딩을 사용하여 현재 파일을 다시로드 합니다. 엠에디터 내에서 문서가 변경 되었다면, "변경 내용을 취소하시겠습니까?"라는 확인 메시지가 나타납니다.
**예** 를 선택하면 변경 사항이 저장되지 않고 취소되며 새로운 내용을 다시 로드합니다. **아니오** 를 선택하면 다시 로드 하는것을 중단하고 그 문서를 계속하여
편집할수 있도록 합니다.

## 실행하는 방법

- 기본 메뉴: **파일** \> **다시 로드** \> **(인코딩)**
- [모든 명령](../tools/all_commands): **파일** \> **다시 로드** \> **(인코딩)**
- 도구 모음: ![](../../images/reload..png) (화살표 위)\-
(인코딩)
- 상태 표시줄: 인코딩을 두 번 클릭 \- (인코딩)
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_FILE_RELOAD_DEFINED through EEID_FILE_RELOAD_DEFINED + 255 (from 6656
```
through
6656 + 255)

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(6656 + i);  // i is an integer from 0
through 255
```

## \[VBScript\]

```
editor.ExecuteCommandByID 6656 + i  ' i is an integer from 0
through 255
```
