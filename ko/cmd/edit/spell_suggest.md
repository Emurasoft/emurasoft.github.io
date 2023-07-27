# 맞춤법 제안 명령

## 요약

올바른 철자의 제안을 선택합니다 (여러 항목).

## 설명

올바른 철자의 제안을 선택하고 맞춤법이 틀린 단어를 제안된 문자로 대체합니다 (문서 전체는 아님).

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>맞춤법 \>(맞춤법 제안)
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_SPELL_SUGGEST through EEID_SPELL_SUGGEST + 31 (from 8768 through 8768 + 31)```

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(8768 + i);  // i is an integer from 0 through 31
```

## \[VBScript\]

```
editor.ExecuteCommandByID 8768 + i  ' i is an integer from 0 through 31
```
