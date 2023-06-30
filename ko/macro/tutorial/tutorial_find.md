# 파일 내에서 찾기 (Ʃ�丮��)

파일 내에서 문자열을 찾으려면, 튜토리얼 매크로에 여덟번째 줄을 추가합니다:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

document.selection.CharRight( true, 9 );

document.selection.ChangeCase( eeCaseUpperCase );

if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

document.selection.CharRight True, 9

document.selection.ChangeCase eeCaseLowerCase

If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"

위의 매크로를 저장하고 새로운 엠에디터 창에 매크로를 실행합니다.
이제, "Em"이 검색되고 "Found!"를 나타내는 텍스트 메시지 박스가 표시됩니다.

[Find 메서드](../selection/selection_find) 의 첫번째 인수는
검색하려는 문자열을 지정하고, 두번째 인수는 검색 방법을 알려주는 플래그를 지정합니다.
이 예문에서는, 두번째 인수가 eeFindPrevious를 사용하고 현재 커서 위치에서부터 파일의 최상단까지 역방향으로
검색을 하게 됩니다.
검색 문자열이 발견되면 [Find 메서드](../selection/selection_find) 는 1로 반환됩니다.
그렇지 않은 경우, 0으로 반환됩니다.
이 예문에서는, 검색 문자열이 발견되어 1이 반환된 후
[alert 메서드](../window/window_alert) 가 실행됩니다.
[alert 메서드](../window/window_alert) 는 OK 버튼과 인수의 문자열을
포함한 간단한 메시지 상자를 표시합니다.
튜토리얼에서는 "Found!" 텍스트를 표시합니다.

[Find 메서드](../selection/selection_find) 의 두번째 인수는
다양한 플래그를 지정할 수 있도록 합니다. 더 자세한 정보는
[Find 메서드](../selection/selection_find) 의 인수 설명을 참고하십시오.

일반적으로, 검색 문자열이 발견되지 않았을 시 매크로의 실행은 중단되지 않습니다.
하지만, 예외의 경우가 있습니다.
**매크로** 메뉴 아래 **임시 옵션으로 실행** 명령에서 **검색 실패시 중지** 체크 박스를 선택하고
매크로를 실행한 경우,
검색 문자열이 발견되지 않았을 시 매크로의 실행을 중단합니다.
**임시 옵션으로 실행** 은 유연한 방법으로 검색을 수행할 수 있도록 합니다.
예를 들어, 검색과 바꾸기와 같은 작업을 반복적으로 수행하고 싶지만 얼마 만큼의 작업을 실행해야 하는지 알지
못하는 경우, 매크로를 수정하지 않고 필요로 생각되는 수보다 크게 작업 반복 수를 지정하여
검색이 실패되었을 때 검색을 중단되도록 할 수 있습니다.

**임시 옵션으로 실행** 명령을 사용하지 않고 검색 실패 시
매크로의 실행을 중단하고 싶은 경우에는 매크로를 수정해야 합니다.
즉, [Find 메서드](../selection/selection_find) 가 0으로 반환되었을 때, 매크로를 중단합니다.
다음의 코드가 그 작업을 할 것입니다:

#### \[JavaScript\]

if( !document.selection.Find( "xx", eeFindPrevious ) )  throw new
Error("Cannot find xx");

#### \[VBScript\]

If Not document.selection.Find( "xx", eeFindPrevious )  Then Err.Raise
vbObjectError + 1, "Find Error", "Cannot find xx"

또한, [FindRepeat 메서드](../selection/selection_findrepeat) 를 사용하는 경우,
이전에 검색에 사용했던 문자열을 다시 검색할 수 있고, 커서가 위치한 곳의 단어를 검색할 수 있습니다.
[FindRepeat 메서드](../selection/selection_findrepeat) 의 플래그를 다음과 같이
지정하는 경우, 해당 키보드 명령 단축키가 있는 검색을 수행합니다.

|     |     |
| --- | --- |
| eeFindRepeatNext | 앞서서 검색에 사용했던 문자열을 현재 커서 위치로부터 앞으로 다시 검색합니다.<br> F3에 해당합니다. |
| eeFindRepeatPrevious | 앞서서 검색에 사용했던 문자열을 현재 커서 위치로부터 뒤로 다시 검색합니다.<br> Shift + F3에 해당합니다. |
| eeFindRepeatNext + eeFindRepeatWord | 선택된 문자열이나 커서가 위치한 단어를 현재 커서 위치로부터 앞으로 검색합니다.<br> CTRL + F3에 해당합니다. |
| eeFindRepeatPrevious + eeFindRepeatWord | 선택된 문자열이나 커서가 위치한 단어를 현재 커서 위치로부터 뒤로 검색합니다.<br> CTRL + SHIFT + F3에 해당합니다. |

## 다음 항목: