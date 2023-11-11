# 문자 삽입 (튜토리얼)

매크로를 사용하여 문자를 삽입하려면, **[Text 속성](../selection/selection_text)** 을
사용합니다. 튜토리얼 파일을 다음과 같이 변경해 봅니다:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
```
두번째 라인에 추가된[NewLine 메서드](../selection/selectionnewline) 는
커서 위치에 새로운 라인을 삽입합니다. 세번째 라인의 코드는 문자열의 시작에 탭 문자를 삽입합니다.
탭 문자는 JavaScript에서는 "\\t" 으로, VBScript에서는 Chr(9)로 표시됩니다.
VBScript 상수 vbTab을 탭 문자로 사용할 수도 있습니다.
아래의 테이블은 두 스크립트 언어에 모두 일반적으로 사용되는 이스케이프 시퀀스를 나열합니다.

### \[JavaScript\]

|     |     |     |
| --- | --- | --- |
| \\b | \\u0008 | 백 스페이스 |
| \\t | \\u0009 | 수평 탭 |
| \\n | \\u000a | 새로운 라인 |
| \\f | \\u000c | 피드 형성 |
| \\r | \\u000d | 캐리지 리턴 |
| \\" | \\u0022 | 큰 따옴표 |
| \\' | \\u0027 | 작은 따옴표 |
| \\\ | \\u005c | 백 슬래시 |
| \\xXX |  | 두 16진수로 지정된 인코딩을 사용한 Latin-1 문자. |
| \\uXXXX |  | 네개의 16진수로 지정된 인코딩을 사용한 유니코드 문자. |

### ![](../../images/g.gif) 참조: [JScript 특수 문자 (Microsoft MSDN Library)](http://msdn.microsoft.com/ko-kr/library/ie/2yfce773(v=vs.94).aspx)

### \[VBScript\]

|     |     |     |
| --- | --- | --- |
| vbCr | Chr(13) | 캐리지 리턴. |
| vbCrLf | Chr(13) & Chr(10) | 캐리지 리턴 \+ 새로운 줄 결합 |
| vbFormFeed | Chr(12) | 피드 형성. |
| vbLf | Chr(10) | 새로운 라인. |
| vbNewLine | Chr(13) & Chr(10) 또는 Chr(10) | 플랫폼 관련 새로운 라인 문자. 윈도우의 vbCrLf에 해당. |
| vbTab | Chr(9) | 수평 탭. |
| vbVerticalTab | Chr(11) | 수직 탭. |

### ![](../../images/g.gif) 참조: [VBScript \ 문자열 상수 (Microsoft MSDN Library)](http://msdn.microsoft.com/ko-kr/library/hh277t8e(v=vs.84).aspx)

## 팁

줄 끝은 \\r (CR)과 \\n (LF)의 결합으로 종료됩니다.
CR과 LF를 별개의 방식으로 사용합니다.
예를 들어, 다음과 같이 입력한 경우:

document.selection.Text = "\\n";

윈도우의 줄 끝 규칙이 아닌 캐리지 리턴(LF)만 삽입됩니다.
엠에디터에서 반환 키를 눌렀을 때, 엠에디터는 그 줄에서 사용되었던 줄 끝 (CR만, LF만, 또는 CR+LF)을 삽입합니다.
엠에디터에서 반환 키를 누를때마다 같은 작동을 원한다면,
**[NewLine 메서드](../selection/selection_newline)** 또는
**[writeln 메서드](../document/document_writeln)** 를 사용하는 것이 좋습니다.
