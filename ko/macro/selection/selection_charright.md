# CharRight 메서드 (Selection ��ü)

커서를 지정된 숫자의 문자만큼 오른쪽으로 이동합니다.

## 

### \[JavaScript\]

```
document.selection.CharRight( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.CharRight [ bExtend [, nCount ] ]
```

## 매개 변수

_bExtend_

선택 사항입니다. 이동한 텍스트가 축소되는지 아닌지 여부를 지정합니다.
기본 값은 false이고 이동한 텍스트는 축소됩니다.

_nCount_

선택 사항입니다. 오른쪽으로 이동할 문자의 수를 지정합니다.
기본값은 1 입니다. 음수인 경우, 이 메서드는 [CharLeft 메서드](selection_charleft) 와 같이 작용합니다. 0인경우, 메서드는 1과 같이 작용합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
