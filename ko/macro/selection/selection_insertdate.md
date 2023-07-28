# InsertDate 메서드 (Selection 개체)

현재 시간과 날짜를 삽입합니다.

## 

### \[JavaScript\]

```
document.selection.InsertDate( nFlags );
```

### \[VBScript\]

```
document.selection.InsertDate [ nFlags ]
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeDateTimeDate | 시간 후 공백 다음으로 날짜를 지정합니다. |
| eeDateDateTime | 날짜 후 공백 다음으로 시간을 지정합니다. |

## 주의

시간과 날짜에 사용되는 형식은 Windows에서
**제어판** 의 **국가 & 언어 옵션** 을 선택한 뒤 **날짜 & 시간** 을
선택하여 구성 가능합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
