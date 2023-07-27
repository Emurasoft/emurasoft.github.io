# Selection 개체

## 속성

|     |     |
| --- | --- |
|[Count](selection_count) | 현재 문서에서 선택된 영역의 수를 검색합니다. |
|[IsActiveEndGreater](selection_isactiveendgreater) | 활성화 지점이 하단의 지점과 동일한 지 여부를 나타냅니다. |
|[IsEmpty](selection_isempty) | 활성화 지점이 기준 위치와 동일한 지 여부를 나타냅니다. |
|[Mode](selection_mode) | 선택 모드를 나타내는 플래그를 설정하거나 검색합니다. |
|[OverwriteMode](selection_overwritemode) | 덮어쓰기 또는 삽입 모드를 나타내는 플래그를 설정하거나 검색합니다. |
|[Text](selection_text) | 선택된 텍스트를 검색하거나 현재 위치에 문자열을 삽입합니다. |

## 메서드

|     |     |
| --- | --- |
|[ChangeCase](selection_changecase) | 선택된 텍스트의 대,소문자를 변경합니다. |
|[ChangeWidth](selection_changewidth) | 선택된 텍스트의 너비를 변경합니다. |
|[CharLeft](selection_charleft) | 커서를 지정된 숫자의 문자만큼 왼쪽으로 이동합니다. |
|[CharRight](selection_charright) | 커서를 지정된 숫자의 문자만큼 오른쪽으로 이동합니다. |
|[ClearBookmark](selection_clearbookmark) | 현재 줄에 책갈피를 지웁니다. |
|[Collapse](selection_collapse) | 활설화 지점에 선택 영역을 축소합니다. |
|[Copy](selection_copy) | 클립보드에 선택 영역을 복사합니다. |
|[CopyLink](selection_copylink) | 클립보드에 커서 위치의 하이퍼링크를 복사합니다. |
|[Cut](selection_cut) | 선택된 텍스트를 클립보드로 이동합니다. |
|[Delete](selection_delete) | 선택 내용을 삭제합니다. |
|[DeleteLeft](selection_deleteleft) | 선택 내용을 삭제하거나 커서에서 왼쪽으로 지정된 숫자 만큼 삭제합니다. |
|[DestructiveInsert](selection_destructiveinsert) | 기존의 텍스트에 덮어쓰기하여 텍스트를 삽입합니다. |
|[DuplicateLine](selection_duplicateline) | 현재의 줄을 중복되게 합니다. |
|[EndOfDocument](selection_endofdocument) | 문서의 끝 지점으로 커서를 이동합니다. |
|[EndOfLine](selection_endofline) | 현재 줄의 끝 지점으로 커서를 이동합니다. |
|[Find](selection_find) | 지정된 문자열을 검색합니다. |
|[FindRepeat](selection_findrepeat) | 같은 문자열로 이전 검색을 반복합니다. |
|[Format](selection_format) | 선택 영역에 새로운 줄을 삽입하거나 삭제합니다. |
|[GetActivePointX](selection_getactivepointx) | 커서 위치에 열 번호를 반환합니다. |
|[GetActivePointY](selection_getactivepointy) | 커서 위치에 줄 번호를 반환합니다. |
|[GetAnchorPointX](selection_getanchorpointx) | 선택 영역의 원점의 열 번호를 반환합니다. |
|[GetAnchorPointY](selection_getanchorpointy) | 선택 영역의 원점의 줄 번호를 반환합니다. |
|[GetBottomPointX](selection_getbottompointx) | 선택 영역의 하단의 열 번호를 반환합니다. |
|[GetBottomPointY](selection_getbottompointy) | 선택 영역의 하단의 줄 번호를 반환합니다. |
|[GetTopPointX](selection_gettoppointx) | 선택 영역의 상단의 열 번호를 반환합니다. |
|[GetTopPointY](selection_gettoppointy) | 선택 영역의 상단의 줄 번호를 반환합니다. |
|[GoToBrace](selection_gotobrace) | 해당하는 대괄호/중괄호로 커서를 이동합니다. |
|[Indent](selection_indent) | 들여쓰기 레벨의 지정된 수 만큼 선택된 줄을 들여쓰기 합니다. |
|[InsertDate](selection_insertdate) | 현재 시간과 날짜를 삽입합니다. |
|[InsertFromFile](selection_insertfromfile) | 커서 위치에 지정된 파일의 내용을 삽입합니다. |
|[LineDown](selection_linedown) | 지정된 줄의 수 만큼 커서를 아래로 이동합니다. |
|[LineOpen](selection_lineopen) | 두 줄 사이에 빈 줄을 삽입합니다. |
|[LineUp](selection_lineup) | 지정된 줄의 수 만큼 커서를 위로 이동합니다. |
|[NewLine](selection_newline) | 커서에 지정된 수만큼의 새로운 줄을 삽입합니다. |
|[NextBookmark](selection_nextbookmark) | 문서 내에서 다음 책갈피로 이동합니다. |
|[OpenLink](selection_openlink) | 커서 위치에 하이퍼링크를 엽니다. |
|[PageDown](selection_pagedown) | 문서 내에서 지정한 페이지 수만큼 아래로 커서를 이동합니다. |
|[PageUp](selection_pageup) | 문서 내에서 지정한 페이지 수만큼 위로 커서를 이동합니다. |
|[Paste](selection_paste) | 커서에 클립보드 내용을 삽입합니다. |
|[PreviousBookmark](selection_previousbookmark) | 문서 내에서 이전 책갈피로 이동합니다. |
|[Replace](selection_replace) | 문서 내 문자열을 대체합니다. |
|[SelectAll](selection_selectall) | 문서 전체를 선택합니다. |
|[SelectLine](selection_selectline) | 커서 위치에 줄을 선택합니다. |
|[SetActivePoint](selection_setactivepoint) | 커서 위치를 이동하고 필요에 따라 선택 영역을 확장합니다. |
|[SetAnchorPoint](selection_setanchorpoint) | 선택 영역의 원점을 설정합니다. |
|[SetBookmark](selection_setbookmark) | 커서 위치에 책갈피를 설정합니다. |
|[SelectWord](selection_selectword) | 커서 위치에 단어 전체를 선택합니다. |
|[StartOfDocument](selection_startofdocument) | 문서의 시작점으로 커서를 이동합니다. |
|[StartOfLine](selection_startofline) | 줄의 시작점으로 커서를 이동합니다. |
|[Tabify](selection_tabify) | 선택 영역의 공백을 탭으로 변환합니다. |
|[TagJump](selection_tagjump) | 커서 위치에 태크로 점프합니다. |
|[UnIndent](selection_unindent) | 들여쓰기 레벨의 지정된 수 만큼 선택된 텍스트로부터 들여쓰기를 제거합니다. |
|[Untabify](selection_untabify) | 선택 영역에서 탭을 공백으로 변환합니다. |
|[WordLeft](selection_wordleft) | 지정된 단어의 수만큼 왼쪽으로 커서를 이동합니다. |
|[WordRight](selection_wordright) | 지정된 단어의 수만큼 오른쪽으로 커서를 이동합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.


```{toctree}
:maxdepth: 1
selection_changecase
selection_changewidth
selection_charleft
selection_charright
selection_clearbookmark
selection_collapse
selection_copy
selection_copylink
selection_count
selection_cut
selection_delete
selection_deleteleft
selection_destructiveinsert
selection_duplicateline
selection_endofdocument
selection_endofline
selection_find
selection_findrepeat
selection_format
selection_getactivepointx
selection_getactivepointy
selection_getanchorpointx
selection_getanchorpointy
selection_getbottompointx
selection_getbottompointy
selection_gettoppointx
selection_gettoppointy
selection_gotobrace
selection_indent
selection_insertdate
selection_insertfromfile
selection_isactiveendgreater
selection_isempty
selection_linedown
selection_lineopen
selection_lineup
selection_mode
selection_newline
selection_nextbookmark
selection_openlink
selection_overwritemode
selection_pagedown
selection_pageup
selection_paste
selection_previousbookmark
selection_replace
selection_selectall
selection_selectline
selection_selectword
selection_setactivepoint
selection_setanchorpoint
selection_setbookmark
selection_startofdocument
selection_startofline
selection_tabify
selection_tagjump
selection_text
selection_unindent
selection_untabify
selection_wordleft
selection_wordright
```
