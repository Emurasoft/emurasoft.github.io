# 중복된 줄 삭제 명령

## 요약

선택 영역 또는 전체 문서안의 중복된 줄을 삭제합니다.

## 설명

선택 영역 또는 전체 문서안의 중복된 줄을 삭제합니다.
중복된 줄의 첫 인스턴스가 유지됩니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **고급** \> **중복된 줄 삭제**
- [모든 명령](../tools/all_commands): **편집** \> **삭제** \> **중복된 줄 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_DELETE_DUPLICATE (4564)```

## 매크로

### \[JavaScript\]

```
document.DeleteDuplicates("",0);
```

### \[VBScript\]

```
document.DeleteDuplicates "",0
```
