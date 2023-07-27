# GetLine 메서드 (Document ��ü)

지정된 줄의 텍스트를 검색합니다.

## 

### \[JavaScript\]

```
str = document.GetLine( yLine [, nFlags ] );
```

### \[VBScript\]

```
str = document.GetLine( yLine [, nFlags ] )
```

## 매개 변수

_yLine_

검색하려는 텍스트의 줄 번호를 지정합니다.

_nFlags_

선택 사항입니다. 다음의 값의 결합을 지정할 수 있습니다.
아무런 값이 지정되지 않은 경우, 반환 코드없이 논리적 좌표가 지정됩니다.

|     |     |
| --- | --- |
| eeGetLineView | 좌표가 보이게 지정됩니다. |
| eeGetLineWithNewLines | 텍스트에 반환 코드를 추가합니다. |

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
