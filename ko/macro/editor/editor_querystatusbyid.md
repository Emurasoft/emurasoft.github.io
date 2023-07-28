# QueryStatusByID 메서드 (Editor 개체)

활성화되고 있으며 선택되어 있는지 지정된 명령의 현재 상태를 검색합니다.

## 

### \[JavaScript\]

```
nStatus = editor.QueryStatusByID( nID );
```

### \[VBScript\]

```
nStatus = editor.QueryStatusByID( nID )
```

## 매개 변수

_nID_

실행할 명령 ID를 나타내는 정수를 지정합니다.
가능한 명령의 목록을 위해[명령 참조](../../cmd/index) 를 참고하십시오.
모든 명령이 가능하거나 지원되지는 않습니다.

## 반환 값

다음의 값들의 결합을 반환합니다.

|     |     |
| --- | --- |
| eeStatusEnabled | 명령이 가능합니다. |
| eeStatusLatched | 명령이 선택되었습니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
