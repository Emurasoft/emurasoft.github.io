# 구조

|     |     |
| --- | --- |
| [ATTR\_INFO](attr_info) | [EE\_GET\_ATTR](../message/ee_get_attr) 메시지에 의해 사용됩니다. |
| [CLIP\_INFO](../structure/clip_info) | [EE\_CLIP\_HISTORY](../message/ee_clip_history) 메시지에 의해 사용됩니다. |
| [CUSTOM\_BAR\_INFO](custom_bar_info) | [Editor\_CustomBarOpen](../macro/editor_custombaropen) 인라인 함수<br> ( [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) 메시지)에 의해 사용됩니다. |
| [CUSTOM\_BAR\_CLOSE\_INFO](custom_bar_close_info) | [EVENT\_CUSTOM\_BAR\_CLOSED 이벤트](../event/index) 에 의해 사용됩니다. |
| [FIND\_REGEX\_INFO](find_regex_info) | [Editor\_FindRegex 인라인 함수](../macro/editor_findregex)<br> ( [EE\_FIND\_REGEX 메시지](../message/ee_find_regex))에 의해 사용됩니다. |
| [GET\_LINE\_INFO](get_line_info) | Editor\_GetLineA 와 Editor\_GetLineW 인라인 함수 (EE\_GET\_LINEA, <br> EE\_GET\_LINEW 메시지)에 의해 사용됩니다. |
| [GREP\_INFOA](grep_infoa) | [Editor\_FindInFilesA 인라인 함수](../macro/editor_findinfilesa),<br> [Editor\_ReplaceInFilesA 인라인 함수](../macro/editor_replaceinfilesa)<br> ( [EE\_FIND\_IN\_FILESA 메시지](../message/ee_find_in_filesa), [EE\_REPLACE\_IN\_FILESA 메시지](../message/ee_replace_in_filesa))에 의해 사용됩니다. |
| [GREP\_INFOW](grep_infow) | [Editor\_FindInFilesW 인라인 함수](../macro/editor_findinfilesw),<br> [Editor\_ReplaceInFilesW 인라인 함수](../macro/editor_replaceinfilesw)<br> ( [EE\_FIND\_IN\_FILESW 메시지](../message/ee_find_in_filesw), [EE\_REPLACE\_IN\_FILESW 메시지](../message/ee_replace_in_filesw))에 의해 사용됩니다. |
| [HISTORY\_INFO](history_info) | [EVENT\_HISTORY 이벤트](../event/index) 에 의해 사용됩니다. |
| [LOAD\_FILE\_INFO\_EX](load_file_info) | [Editor\_LoadFileA](../macro/editor_loadfilea) 와<br> [Editor\_LoadFileW](../macro/editor_loadfilew) <br>인라인 함수 ( [EE\_LOAD\_FILEA](../message/ee_load_filea) 와<br>[EE\_LOAD\_FILEW](../message/ee_load_filew) 메시지)에 의해 사용됩니다. |
| [MATCH\_REGEX\_INFO](match_regex_info) | [Editor\_MatchRegex 인라인 함수](../macro/editor_matchregex)<br> ( [EE\_MATCH\_REGEX 메시지](../message/ee_match_regex))에 의해 사용됩니다. |
| [OUTLINE\_ARRAY\_INFO](outline_array_info) | [Editor\_SetOutlineArray](../macro/editor_setoutlinearray) <br>인라인 함수( [EE\_SET\_OUTLINE\_ARRAY](../message/ee_set_outline_array) 메시지)에 의해 사용됩니다. |
| [POINT\_PTR](point_ptr) | 포인트 위치를 지정하는데 사용됩니다. 32 비트 플러그 인에서 POINT\_PTR은 POINT 구조와 동일합니다.<br> 64 비트 플러그 인에서 각 필드는 32비트 정수부터 64비트 정수로 확장됩니다. |
| [REG\_QUERY\_VALUE\_INFO](reg_query_value_info) | [EE\_REG\_QUERY\_VALUE 메시지](../message/ee_reg_query_value) 에 의해 사용됩니다. |
| [REG\_SET\_VALUE\_INFO](reg_set_value_info) | [EE\_REG\_SET\_VALUE 메시지](../message/ee_reg_set_value) 에 의해 사용됩니다. |
| [RUN\_MACRO\_INFO](run_macro_info) | [EE\_RUN\_MACRO](../message/ee_run_macro) 메시지에 의해 사용됩니다. |
| [SEL\_INFO](../../plugin/structure/sel_info) | Editor\_GetMultiSel 인라인 함수<br> ( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) 메시지)에 의해 사용됩니다. |
| [SIZE\_PTR](size_ptr) | 크기를 지정하는데 사용됩니다. 32 비트 플러그 인에서 SIZE\_PTR은 SIZE 구조와 동일합니다.<br> 64 비트 플러그 인에서 각 필드는 32비트 정수부터 64비트 정수로 확장됩니다. |
| [TEMP\_INFO](temp_info) | [EE\_EDIT\_TEMP](../message/ee_edit_temp) 메시지와<br> [EVENT\_TEMP\_SAVING 이벤트](../event/index) 에 의해 사용됩니다. |
| [TOOLBAR\_INFO](toolbar_info) | Used by [Editor\_ToolbarOpen 인라인 함수](../macro/editor_toolbaropen)<br> ( [EE\_TOOLBAR\_OPEN 메시지](../message/ee_toolbar_open))와 사용자 지정 도구 모음에 관련된<br> 이벤트에 의해 사용됩니다. |


```{toctree}
:maxdepth: 1
attr_info
clip_info
custom_bar_close_info
custom_bar_info
find_regex_info
get_line_info
grep_infoa
grep_infow
history_info
load_file_info
match_regex_info
outline_array_info
point_ptr
reg_query_value_info
reg_set_value_info
run_macro_info
sel_info
size_ptr
temp_info
toolbar_info
```
