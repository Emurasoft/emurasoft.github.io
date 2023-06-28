# GET\_LINE\_INFO

Editor\_GetLineA 와 Editor\_GetLineW 인라인 함수 (EE\_GET\_LINEA,
EE\_GET\_LINEW 메시지)에 의해 사용됩니다.

typedef struct \_GET\_LINE\_INFO {

UINT cch;

UINT flags;

UINT yLine;

BYTE byteCrLf;

} GET\_LINE\_INFO;

## 필드

_cch_

> 버퍼에 복사할 문자의 최대 수를 지정합니다.
> ( [Editor\_GetLine](../macro/editor_getlinea)
> 매크로의 szString 매개 변수 또는 NULL 문자를 포함하는 [EE\_GET\_LINE](../message/ee_get_linea) 메시지의 lParam). 0이 지정된 경우, Editor\_GetLine 매크로 또는 EE\_GET\_LINE
> 메시지에 의한 반환 값은 텍스트를 수신할 수 있는 버퍼를 위해 문자로 나타낸 필요한 크기입니다.

_flags_

> 이 매개 변수의 하위 단어는 다음의 값들의 결합입니다.
>
> |     |     |
> | --- | --- |
> | FLAG\_LOGICAL | 논리 좌표 _yLine_ 로 _yLine_ 필드를 지정합니다. |
> | FLAG\_WITH\_CRLF | 텍스트에 반환 코드를 추가합니다. |
> | FLAG\_GET\_CRLF\_BYTE | 반환 방법을 나타내는 flag와 채워질 _byteCrLf_ 필드를 지시합니다. FLAG\_LOGICAL 또한 <br> 지정되어야 합니다. |
>
> 이 매개 변수의 상위 단어는 대상 문서의 인덱스입니다. flag의 상위 단어에 1로 시작하는 인덱스를 지정해야 합니다. flag의 상위
> 단어에 0이 지정된 경우, 현재 활성화중인 문서가 대상으로 지정됩니다.

_yLine_

> 검색할 텍스트의 줄 수를 지정합니다.

_byteCrLf_

> 지정된 줄의 반환 메서드를 나타내는 flag를 검색합니다. 이 필드는 flag 필드에 FLAG\_LOGICAL과
> FLAG\_GET\_CRLF\_BYTE이 모두 지정되었을 때에만 사용됩니다. 다음의 값들 중 하나가 됩니다.
>
> |     |     |
> | --- | --- |
> | 0 | CR+LF 또는 파일의 끝 |
> | FLAG\_CR\_ONLY | CR만. |
> | FLAG\_LF\_ONLY | LF만. |