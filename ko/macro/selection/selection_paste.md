# Paste 메서드 (Selection ��ü)

커서에 클립보드 내용을 삽입합니다.

## 

### \[JavaScript\]

```
document.selection.Paste( nFlags );
```

### \[VBScript\]

```
document.selection.Paste nFlags
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeCopyUnicode | 유니코드로 붙여넣습니다 (기본값). |
| eeCopyQuotes | 따옴표 안에 붙여넣습니다. |
| eeCopyNL | 새로운 줄과 붙여넣습니다. |
| eeCopySystemDefault | [시스템 초기 인코딩](../../glossary/systemdefaultencoding) 으로 붙여넣습니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
