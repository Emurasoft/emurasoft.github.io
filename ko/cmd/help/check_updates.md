# 업데이트 확인 명령

## 요약

Emurasoft 서버에 연결하여 엠에디터 새로운 버전의 업데이트가 가능한지 확인합니다.

## 설명

Emurasoft 서버에 연결하여 엠에디터 새로운 버전의 업데이트가 가능한지 확인합니다.
이 작업을 하기 위해서는 인터넷 연결이 필요합니다.
엠에디터에서 업데이트 확인이 완료된 후, 업데이트가 가능한 경우 업데이트 시작에 대한 메시지가 표시됩니다.

## 실행하는 방법

- 기본 메뉴: **도움말** \> **업데이트 확인 명령**
- [모든 명령](../tools/all_commands): **도움말** >
**업데이트 확인 명령**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_CHECK_UPDATES (4481)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4481);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4481
```
