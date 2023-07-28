# Japanese JIS으로 저장 명령

## 요약

Japanese JIS 인코딩을 사용하여 현재 파일을 저장합니다.

## 설명

이 명령은 문서의 제목이 정해져 있지 않는 한, 현재의 파일 이름으로 Japanese JIS 인코딩을 사용하여 문서를 저장합니다.
문서의 제목이 정해져 있지 않다면 저장하기 원하는 파일 이름을 입력할 수 있는 **다른 이름으로 저장** 대화 상자가 나타나게 됩니다.

이 명령은 엠에디터의 이전 버전과의 호환성을 위해 유지되고 있습니다. 이 명령을 대신하여 [**인코딩으로 저장하기 (여러 항목)** 명령](file_save_defined) 을
사용할 수 있고 Japanese JIS를 지정할수 있습니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **저장**
\> **인코딩으로 저장** \> **Japanese JIS로 저장**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_FILE_SAVE_JIS (4103)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4103);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4103
```
