# Document 개체

## 속성

|     |     |
| --- | --- |
|[Config](config) | Config 개체를 검색합니다. |
|[ConfigName](document_configname) | 현재 구성 이름을 검색하거나 설정합니다. |
|[Encoding](document_encoding) | 열린 파일의 현재 인코딩을 검색하거나 설정합니다. |
|[FontCategory](document_fontcategory) | 현재 글꼴 범주를 검색하거나 설정합니다. |
|[FullName](document_fullname) | 문서의 전체 경로와 파일 이름을 검색합니다. |
|[HighlightFind](document_hightlightfind) | 검색된 문자열을 강조 표시 할지의 여부를 결정합니다. |
|[HighlightTag](document_hightlighttag) | 태그를 강조 표시 할자의 여부를 결정합니다. |
|[Name](document_name) | 현재 문서의 파일 이름만을 검색합니다. |
|[Path](document_path) | 현재 문서의 경로만을 검색합니다. |
|[ReadOnly](document_readonly) | 문서의 읽기 전용 상태를 설정합니다. |
|[Saved](document_saved) | 마지막으로 저장되거나 열린 후로 문서가 수정되었는지 여부를 나타내는 플래그를 검색하거나 설정합니다. |
|[selection](document_selection) | Selection 개체를 검색합니다. |
|[UnicodeSignature](document_unicodesignature) | 엠에디터가 다음 번에 문서를 저장할 때 유니코드 서명(BOM)을 추가해야 하는지<br> 여부를 나타내는 플래그를 검색하거나 설정합니다. |

## 메서드

|     |     |
| --- | --- |
|[Activate](document_activate) | 문서를 활성화합니다. |
|[close](document_close) | 문서를 닫습니다. |
|[CopyFullName](document_copyfullname) | 클립보드에 문서의 전체 경로와 파일 이름을 복사합니다. |
|[CopyPath](document_copypath) | 클립보드에 문서의 경로만을 복사합니다. |
|[GetLine](getline) | 지정된 줄의 텍스트를 검색합니다. |
|[GetLines](getlines) | 문서의 줄 수를 검색합니다. |
|[Redo](document_redo) | [실행 취소 명령](../../cmd/edit/edit_undo) 으로<br> 실행을 취소한 마지막 동작을 다시 실행합니다. |
|[Save](document_save) | 문서를 저장합니다. |
|[Undo](document_undo) | 마지막 동작을 실행 취소합니다. |
|[write](document_write) | 현재 커서 위치에 문자열을 삽입하거나 덮어쓰기합니다. |
|[writeln](document_writeln) | 현재 커서 위치에 문자열과 새 줄을 삽입하거나 덮어쓰기합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.


```{toctree}
:maxdepth: 1
config
document_activate
document_close
document_configname
document_copyfullname
document_copypath
document_encoding
document_fontcategory
document_fullname
document_hightlightfind
document_hightlighttag
document_name
document_path
document_readonly
document_redo
document_save
document_saved
document_selection
document_undo
document_unicodesignature
document_write
document_writeln
getline
getlines
```
