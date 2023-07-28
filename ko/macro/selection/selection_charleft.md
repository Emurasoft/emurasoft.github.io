# CharLeft 메서드 (Selection 개체)

커서를 지정된 숫자의 문자만큼 왼쪽으로 이동합니다.

## 

### \[JavaScript\]

```
document.selection.CharLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.CharLeft [ bExtend [, nCount ] ]
```

## 매개 변수

_bExtend_

선택 사항입니다. 이동한 텍스트가 축소되는지 아닌지 여부를 지정합니다.
기본 값은 false이고 이동한 텍스트는 축소됩니다.

_nCount_

선택 사항입니다. 왼쪽으로 이동할 문자의 수를 지정합니다.
기본 값은 1입니다. 음수인 경우, 메서드는 [CharRight \
메서드](selection_charright) 와 같이 작용합니다. 0인 경우, 메서드는 1과같이 작용합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
