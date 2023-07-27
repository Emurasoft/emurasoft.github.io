# 플러그 인 메시지

|     |     |
| --- | --- |
|메시지 |설명 |
| [EP\_DISABLE\_AUTO\_COMPLETE](ep_disable_auto_complete) | 자동 완성 괄호/따옴표 표시 기능이 비활성화 되어야 하는지 여부를 검색합니다. |
| [EP\_GET\_BITMAP](ep_get_bitmap) | 도구 모음에 표시되는 플러그 인의 다양한 크기와 색 농도를 위해 비트맵 resource IDs를 검색합니다. |
| [EP\_GET\_INFO](ep_get_info) | 플러그 인에 관한 정보를 검색합니다. |
| [EP\_GET\_MASK](ep_get_mask) | 도구 모음에 플러그 인 버튼을 위한 마스크 색상을 검색합니다. |
| [EP\_GET\_NAME](ep_get_name) | 플러그 인 이름을 검색합니다. |
| [EP\_GET\_VERSION](ep_get_version) | 플러그 인 버전을 검색합니다. |
| [EP\_QUERY\_PROPERTIES](ep_query_properties) | 속성이 활성화 되어 있는지 여부를 검색합니다. |
| [EP\_QUERY\_UNINSTALL](ep_query_uninstall) | 플러그 인이 제거 가능한 지 여부를 검색합니다. |
| [EP\_SET\_PROPERTIES](ep_set_properties) | 속성을 나타내기위해 플러그 인을 요청합니다. |
| [EP\_SET\_UNINSTALL](ep_set_uninstall) | 플러그 인을 제거합니다. |
| [EP\_PRE\_TRANSLATE\_MSG](ep_pre_translate_msg) | 각 Windows 메시지가 번역되기 이전에 호출됩니다. |
| [EP\_USE\_DROPPED\_FILES](ep_use_dropped_files) | 플러그 인이 삭제된 파일을 사용하기 원하는 지 여부를 검색합니다. |

이러한 메시지는 [플러그 인 내보내기 기능 PlugInProc](../exports/index) 에 의해 사용됩니다.

이러한 상수는 [헤더 파일 (plugin.h)](https://download.emeditor.info/include/plugin.h) 에서 정의됩니다.


```{toctree}
:maxdepth: 1
ep_disable_auto_complete
ep_get_bitmap
ep_get_info
ep_get_mask
ep_get_name
ep_get_version
ep_pre_translate_msg
ep_query_properties
ep_query_uninstall
ep_set_properties
ep_set_uninstall
ep_use_dropped_files
```
