# Item 속성 (DisplayList 컬렉션)

지정된 인덱스를 위한 [DisplayItem 개체](../display_item/index) 를 검색합니다.

## 

### \[JavaScript\]

```
item = list.Item( Index );
```

### \[VBScript\]

```
item = list.Item( Index )
```

## 매개 변수

_Index_

1부터 시작하는 정수로된 항목의 인덱스를 지정합니다.

개체가 색상의 목록인 경우에는 다음의 값중 하나여야만 합니다.

|     |     |
| --- | --- |
| eeColorNormal | 일반 |
| eeColorSelection | 선택 |
| eeColorCurrentLine | 현재 줄 |
| eeColorQuote | 따옴표된 줄 |
| eeColorURL | URL |
| eeColorMailTo | 메일 주소 |
| eeColorTag | 파일 내 찾기 하이퍼 링크 |
| eeColorSingleQuotes | 작은 따옴표로 닫힌 문자열 '...' |
| eeColorDoubleQuotes | 큰 따옴표로 닫힌 문자열 "..." |
| eeColorComment | 주석 |
| eeColorScript | 스크립트 |
| eeColorBraces | 일치하는 괄호/대괄호 |
| eeColorInsideTag | 태그 |
| eeColorHighlight1 | 강조표시 (1) |
| eeColorHighlight2 | 강조표시 (2) |
| eeColorHighlight3 | 강조표시 (3) |
| eeColorHighlight4 | 강조표시 (4) |
| eeColorHighlight5 | 강조표시 (5) |
| eeColorHighlight6 | 강조표시 (6) |
| eeColorHighlight7 | 강조표시 (7) |
| eeColorHighlight8 | 강조표시 (8) |
| eeColorHighlight9 | 강조표시 (9) |
| eeColorHighlight10 | 강조표시 (10) |
| eeColorReturn | 반환, 탭, EOF |
| eeColorCursorLine | 가로/세로 줄 |
| eeColorPageBreak | 페이지 분리 표시 |
| eeColorLineNumbers | 줄 번호 (자릿수) |
| eeColorRuler | 눈금자 (자릿수) |
| eeColorOutside | 영역 이외 |
| eeColorCompareChange | 변경된 줄 비교 |
| eeColorCompareChar | 변경된 문자 비교 |
| eeColorCompareAdded | 비교 \- 추가됨 |
| eeColorCompareDeleted | 비교 \- 삭제됨 |
| eeColorCompareBlank | 비교 \- 공백 |
| eeColorSpell | 틀린 맞춤법 |
| eeColorUnicode | 유니코드 문자 |
| eeColorVerticalSel | 세로 선택 영역 프레임 |
| eeColorHexSel | 16진수 보기 선택 영역 프레임 |
| eeColorIndentGuides | 들여쓰기 가이드 |
| eeColorHorzGrid | 가로 눈금 |
| eeColorOutline | 윤곽 |
| eeColorLineNumberLines | 줄 번호 (줄) |
| eeColorRulerLines | 눈금자 (줄) |
| eeColorVerticalSeparator | 수직 구분 |
| eeColorHtmlCharRef | HTML 문자 참조 |
| eeColorUcn | 유니버설 문자 이름 |
| eeColorAutoMarker | 자동 마커 |
| eeColorMarker1 | 마커 (1) |
| eeColorMarker2 | 마커 (2) |
| eeColorMarker3 | 마커 (3) |
| eeColorMarker4 | 마커 (4) |
| eeColorMarker5 | 마커 (5) |
| eeColorMarker6 | 마커 (6) |
| eeColorMarker7 | 마커 (7) |
| eeColorMarker8 | 마커 (8) |
| eeColorMarker9 | 마커 (9) |
| eeColorMarker10 | 마커 (10) |
| eeColorMatchingTag | 대응태그 |
| eeColorBookmark | 책갈피된 줄 |
| eeColorUserDefinedGuides | 사용자 지정 가이드 |
| eeColorIndicatorModified | 수직 표시기 \- 변경된 줄 |
| eeColorIndicatorSaved | 수직 표시기 \- 저장된 줄 |
| eeColorIndicatorBookmark | 수직 표시기 \- 책갈피 |
| eeColorMarkerModified | 스크롤 바 마커 \- 변경된 줄 |
| eeColorMarkerSaved | 스크롤 바 마커 \- 저장된 줄 |
| eeColorMarkerBookmark | 스크롤 바 마커 \- 책갈피 |
| eeColorMarkerFound | 스크롤 바 마커 \- 찾음 |
| eeColorMarkerCursor | 스크롤 바 마커 \- 커서 위치 |
| eeColorMarkerCompareChange | 스크롤 바 마커 \- 변경된 줄 비교 |
| eeColorMarkerCompareAdded | 스크롤 바 마커 \- 추가됨 비교 |
| eeColorMarkerCompareDeleted | 스크롤 바 마커 \- 삭제됨 비교 |
| eeColorHeadings | 제목 |
| eeColorSearchSel | 검색 범위 |
| eeColorFilter | 필터 |
| eeColorLinkUrlVisited | URLs (방문함) |
| eeColorLinkIdVisited | 우편 주소 (방문함) |
| eeColorLinkTagVisited | 파일 하이퍼링크에서 찾기 (방문함) |
| eeColorCellText | CSV 셀 선택된 텍스트 |
| eeColorCellBorder | CSV 셀 선택 프레임 |

개체가 검색의 목록인 경우에는, 검색이 만들어진 시간 단위 수를 지정합니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
