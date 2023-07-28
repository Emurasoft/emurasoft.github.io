# 엠에디터 Professional과 엠에디터 Standard의 새로운 기능

## 새로운 명령

- [항상 상위 \- 켜기](../cmd/window/window_always_top_on)
- [항상 상위 \- 끄기](../cmd/window/window_always_top_off)

## 새로운 옵션과 기존 대화 상자

- [대화 상자 사용자 지정](../dlg/customize/index)
- [구성 속성](../dlg/properties/index) 에 있는 [파일 탭](../dlg/properties/file/index)

## 다른 새로운 기능

- [**파일 내 찾기**](../cmd/search/grep) 를 하는 동안 취소할 수 있습니다.
- [**파일 내 찾기**](../cmd/search/grep) 를 하기 위해 정규식을 사용하는 멀티바이트 문자를 이용할 수 있습니다.
- 정규식을 이용하기위한 검색이 더 빨라집니다.
- 엠에디터가 다른 창을 검색하는 방법이 최적화되었고, 엠에디터를 시작하는 시간이 더 빨라졌습니다.
- **도움말** 버튼을 각각의 대화상자에 추가해 주십시오.
- **[명령 참고](../cmd/index)** 를 포함하는 세부 사항이
도움말과 **[자주 묻는 질문](../faq/index)** 과 함께 더욱 향상되었습니다.
- 윈도우 2000/XP/2003 에서, 중심과 몇몇의 대화 상자 뿐만이 아니라 모든 대화 상자가 유니코드를 지원합니다.
- Added the /? 스위치가 **[명령줄 옵션](../howto/file/file_commandline)** 에 추가되었습니다.
- an inserted string can be undone with only one
[**취소** 명령](../cmd/edit/edit_undo).
이 행동은 [**사용자 지정** 대화 상자](../dlg/customize/index) 의
[**고급** 탭](../dlg/customize/advanced/index) 에서
**문자별 취소(엠에디터를 다시 시작해야 합니다.)** 체크 박스에 체크를 지우는 방법을 이용해서 이전 행동으로 복구될 수 있습니다.
- Read Me 파일(엠에디터.txt)을 제거하고 모든 정보를 도움말로 통합하였습니다.
- 새로운 플러그인 메시지를 추가하였습니다. [EE\_SET\_SEL\_TYPE](../plugin/message/ee_set_sel_type), [EE\_GET\_STATUSA](../plugin/message/ee_get_statusa),
[EE\_GET\_STATUSW](../plugin/message/ee_get_statusw),
[EE\_INSERT\_FILEA](../plugin/message/ee_insert_filea),
[EE\_INSERT\_FILEW](../plugin/message/ee_insert_filew),
[EE\_GET\_ANCHOR\_POS](../plugin/message/ee_get_anchor_pos),
[EE\_SET\_ANCHOR\_POS](../plugin/message/ee_set_anchor_pos)

또한, 기존 메시지를 새로운 기능과 함께 확장했습니다.
[EE\_INSERT\_STRINGA](../plugin/message/ee_insert_stringa),
[EE\_INSERT\_STRINGW](../plugin/message/ee_insert_stringw),
[EE\_GET\_VERSION](../plugin/message/ee_get_version),
[EE\_INFO](../plugin/message/ee_info),
[EE\_SET\_CARET\_POS](../plugin/message/ee_set_caret_pos)
- **확인**, **자동 다시 로드**, 혹은 **잠금 유지** 옵션으로
[**다른 프로그램으로 바꾸기** \
드롭다운 리스트 상자](../dlg/properties/file/index) 로 파일이 읽기전용 속성이 바뀌었을 때 엠에디터를 읽기 전용 상태로 바꿀 수 있습니다.
