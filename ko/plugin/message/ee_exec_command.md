# EE\_EXEC\_COMMAND

지정된 명령을 실행합니다. 이 메시지를 명시적으로 보내거나
[Editor\_ExecCommand](../macro/editor_execcommand) 인라인 함수를 사용할 수 있습니다.

```
EE_EXEC_COMMAND
wParam = (WPARAM) (UINT) nCmdID;
lParam = 0;
```

## 매개 변수

_nCmdID_

실행될 명령의 식별자입니다. [Command IDs](../cmdid/index) 를 참고하십시오.

## 반환 값

반환 값이 사용되지 않습니다.
