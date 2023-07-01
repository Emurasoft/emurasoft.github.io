# Editor\_ExecCommand

지정된 명령을 실행합니다. 이 인라인 함수를 사용하거나 [EE\_EXEC\_COMMAND](../message/ee_exec_command)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_ExecCommand( HWND hwnd, UINT nCmdID );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nCmdID_

> 실행할 명령의 식별자입니다. [Command IDs](../cmdid/index) 를 참고하십시오.

## 반환 값

> 반환 값이 사용되지 않습니다.
