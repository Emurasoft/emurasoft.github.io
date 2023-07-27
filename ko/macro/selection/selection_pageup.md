# PageUp 메서드 (Selection ��ü)

문서 내에서 지정한 페이지 수만큼 위로 커서를 이동합니다.

## 

### \[JavaScript\]

```
document.selection.PageUp( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.PageUp [ bExtend [, nCount ] ]
```

## 매개 변수

_bExtend_

선택 사항입니다. 이동한 텍스트가 축소하였는지 아닌지의 여부를 지정합니다. 기본값은 false이고 이동한 텍스트는 축소됩니다.

_nCount_

선택 사항입니다.
위로 이동할 페이지의 수를 지정합니다. 기본 값은 1 입니다.
음수인 경우, 이 메서드는 [PageDown \
메서드](selection_pagedown) 와 동일하게 작용합니다. 0인 경우, 메서드는 1과 동일하게 작용합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
