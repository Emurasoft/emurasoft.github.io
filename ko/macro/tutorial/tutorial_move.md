# 커서 이동 (튜토리얼)

커서를 이동하려면, 튜토리얼 매크로에 다음과 같은 네번째 라인을 추가합니다:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
```
매크로를 저장하고 새로운 엠에디터 창에서 실행합니다.
커서가 줄의 끝에서 왼쪽으로 12자 옆으로 옮겨졌거나,
"text editor"의 첫번째 't'문자로 옮겨진 것을 알 수 있습니다.
[CharLeft 메서드](../selection/selectioncharleft) 는
커서를 지정된 숫자의 문자만큼 왼쪽으로 이동합니다.
[CharLeft 메서드](../selection/selectioncharleft) 의
첫번째 인수 (false)는 선택 범위를 변경할 것인지 여부를 지정합니다. 즉,
키보드에서 왼쪽 화살표 키를 사용할 때 SHIFT 키를 사용할지 여부를 지정합니다.
아래의 메서드는 커서의 움직임을 조작하는데 제공됩니다:
|     |     |
| --- | --- |
|[CharLeft](../selection/selectioncharleft) | 지정된 숫자의 문자만큼 왼쪽으로 커서를 이동합니다. 왼쪽 화살표 키에 해당합니다. |
|[CharRight](../selection/selectioncharright) | 지정된 숫자의 문자만큼 오른쪽으로 커서를 이동합니다. 오른쪽 화살표 키에 해당합니다. |
|[LineDown](../selection/selectionlinedown) | 지정된 숫자의 문자만큼 아래쪽으로 커서를 이동합니다. 아래쪽 화살표 키에 해당합니다. |
|[LineUp](../selection/selectionlineup) | 지정된 숫자의 문자만큼 위쪽으로 커서를 이동합니다. 위쪽 화살표 키에 해당합니다. |
|[WordLeft](../selection/selectionwordleft) | 한 단어 왼쪽으로 커서를 이동합니다. CTRL + 왼쪽 화살표에 해당합니다. |
|[WordRight](../selection/selectionwordright) | 한 단어 오른쪽으로 커서를 이동합니다. CTRL + 오른쪽 화살표에 해당합니다. |
|[PageDown](../selection/selectionpagedown) | 한 탭 아래로 커서를 이동합니다. PAGE DOWN 키에 해당합니다. |
|[PageUp](../selection/selectionpageup) | 한 페이지 위로 커서를 이동합니다. PAGE UP 키에 해당합니다. |
|[StartOfLine](../selection/selectionstartofline) | 문장의 시작점으로 커서를 이동합니다. HOME 키에 해당합니다. |
|[EndOfLine](../selection/selectionendofline) | 문장의 끝 지점으로 커서를 이동합니다. END 키에 해당합니다. |
|[StartOfDocument](../selection/selectionstartofdocument) | 문서의 처음으로 커서를 이동합니다. CTRL+ HOME에 해당합니다. |
|[EndOfDocument](../selection/selectionendofdocument) | 문서의 마지막으로 커서를 이동합니다. CTRL+ END에 해당합니다. |
|[GoToBrace](../selection/selectiongotobrace) | 일치하는 괄호로 커서를 이동합니다. |

다음의 메서드는 커서를 지정된 라인이나 자리 위치로 이동합니다.
|     |     |
| --- | --- |
|[SetActivePoint](../selection/selectionsetactivepoint) | 커서 위치를 설정합니다. |
