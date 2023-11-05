# EE\_CLIP\_HISTORY

클립보드 기록을 조작합니다. 이 메시지를 명시적 또는 [Editor\_GetClip](../macro/editor_getclip), [Editor\_GetClipPos](../macro/editor_getclippos), [Editor\_InsertClip](../macro/editor_insertclip),
[Editor\_RemoveClip](../macro/editor_removeclip), [Editor\_RotateClip](../macro/editor_rotateclip),
및 [Editor\_SetClipPos](../macro/editor_setclippos) 인라인 함수를 사용하여 보낼 수 있습니다.

```
EE_CLIP_HISTORY
wParam = 0;
lParam = (LPARAM) (CLIP_INFO) pCI;
```

## 매개 변수

_pTI_

[CLIP\_INFO](../structure/clip_info) 구조에 대한 포인터 입니다.

## 반환 값

메시지가 실패한 경우, 반환 값은 -1입니다.
메시지가 성공하면 반환 값은 CLIP\_INFO 구조의 nAction 매개 변수로 지정된 값에 의해 결정됩니다.
nAction 매개 변수가 CI\_GET\_CLIP인 경우, 반환 값은 종료된 NULL을 포함한 텍스트를 수신하는데 필요한 문자 내
pszBuf 버퍼의 크기입니다. nAction 매개 변수가 CI\_INSERT\_CLIP인 경우, 반환 값은 클립보드 기록 내
새로운 텍스트가 삽입된 위치입니다. nAction 매개 변수가 CI\_REMOVE\_CLIP인 경우, 반환 값은 클립보드
기록 내 텍스트가 삭제된 위치입니다. nAction 매개 변수가 CI\_GET\_CLIP\_POS인 경우, 반환 값은 클립보드 기록의
현재 위치입니다. nAction 매개 변수가 CI\_SET\_CLIP\_POS인 경우, 반환 값은 클립보드 기록의 이전 위치입니다.
nAction 매개 변수가 CI\_ROTATE\_CLIP인 경우, 반환 값은 1입니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
