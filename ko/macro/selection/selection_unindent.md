# UnIndent 메서드 (Selection 개체)

들여쓰기 레벨의 지정된 수 만큼 선택된 텍스트로부터 들여쓰기를 제거합니다.

## 

### \[JavaScript\]

```
document.selection.UnIndent( [ nCount ] );
```

### \[VBScript\]

```
document.selection.UnIndent [ nCount ]
```

## 매개 변수

_nCount_

선택 사항입니다. 들여쓰기 수준의 번호를 지정합니다.
기본 값은 1 입니다. 음수인 경우, 메서드는 [**Indent**메서드](selection_indent) 와 동일하게 작용합니다. 0인 경우, 메서드는 1과 동일하게 작용합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
