# 이름 변경 후 저장 명령

## 요약

현재 파일의 이름을 변경한 후 저장합니다.

## 설명

[**다른 이름으로 저장** 명령](file_save_as) 과는 다르게, 이 명령은 현재 파일의 이름을 변경한후 기존 파일을 삭제합니다.
이 명령은 현재 열려있는 파일을 저장할 때 파일 이름을 입력할 수 있는 **다른 이름으로 저장** 대화 상자를 나타냅니다.
새로운 파일 이름을 지정한 후에 "삭제 하시겠습니까?"라는 확인 메시지가 나타납니다.
**예** 를 선택하면 기존의 이름을 가졌던 파일은 삭제됩니다.
**아니오** 를 선택하면 기존의 이름을 삭제하지는 않지만 [**다른 이름으로 저장** 명령](file_save_as) 와 같은 방식으로 새로운 이름의 파일을 저장합니다.

다른 이름으로 파일을 저장하지만 기존의 파일을 삭제하기 원치 않으시면 [**다른 이름으로 저장** 명령](file_save_as) 을 대신 사용하시기 바랍니다.

## 실행하는 방법

- 기본 메뉴: **파일** \> **이름 변경 후 저장**
- [모든 명령](../tools/all_commands): **파일** \> **저장**
\> **이름 변경 후 저장**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_FILE_SAVE_RENAME (4252)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4252);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4252
```
