# EndOfLine 메서드 (Selection 개체)

현재 줄의 끝 지점으로 커서를 이동합니다.

## 

### \[JavaScript\]

```
document.selection.EndOfLine( [ bExtend [, nFlags ] ] );
```

### \[VBScript\]

```
document.selection.EndOfLine [ bExtend [, nFlags ] ]
```

## 매개 변수

_bExtend_

선택 사항입니다. 이동한 텍스트가 축소하였는지 아닌지의 여부를 지정합니다. 기본값은 false이고 이동한 텍스트는 축소됩니다.

_nFlags_

선택 사항입니다. 다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeLineView | 보이기 선을 지정합니다. |
| eeLineLogical | 논리적 선을 지정합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
