# EE\_SET\_MODIFIED

텍스트의 수정된 상태를 변경합니다. 이 메시지를 명시적으로 또는 [Editor\_SetModified](../macro/editor_setmodified) 인라인 함수를 사용하여 보낼 수 있습니다.

```
EE_SET_MODIFIED
wParam = (WPARAM) (BOOL) bModified;
lParam = 0;
```

## 매개 변수

_bModified_

수정됨으로 상태를 변경하려면 TRUE를, 수정되지 않음으로 상태를 변경하려면 FALSE입니다.

## 반환 값

반환 값이 사용되지 않습니다.
