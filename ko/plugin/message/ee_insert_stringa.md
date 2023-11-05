# EE\_INSERT\_STRINGA

현재 커서 위치에 ANSI 문자열을 삽입합니다. 이 메시지를 명시적으로 보내거나
[Editor\_InsertStringA \
macro](../macro/editor_insertstringa), [Editor\_InsertA macro](../macro/editor_inserta), 또는
[Editor\_OverwriteA](../macro/editor_overwritea) 인라인 함수를 사용할 수
있습니다.

```
EE_INSERT_STRINGA
wParam = nInsertType;
lParam = (LPARAM) (LPCSTR) szString;
```

## 매개 변수

_nInsertType_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| OVERWRITE\_PER\_PROP | 현재 삽입하기/덮어쓰기 상태에 따라 삽입하거나 덮어씁니다. |
| OVERWRITE\_INSERT | 항상 삽입하고 기존의 문자열에 덮어쓰지 않습니다. |
| OVERWRITE\_OVERWRITE | 항상 기존의 문자열에 덮어씁니다. |
| KEEP\_SOURCE\_RETURN\_TYPE | szString 매개 변수에 지정된 반환 유형 (CR 만, LF 만 또는 CR과 LF)을 유지합니다. |
| KEEP\_DEST\_RETURN\_TYPE | 대상 반환 유형 (CR 만, LF 만 또는 CR과 LF)을 유지합니다. |

_szString_

삽입할 문자열을 지정합니다.

## 반환 값

반환 값이 사용되지 않습니다.

## 버전

KEEP\_SOURCE\_RETURN\_TYPE 과 KEEP\_DEST\_RETURN\_TYPE flags는 EmEditor 버전 7 이상에서만 지원됩니다.
