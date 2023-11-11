# 문자열 대체 (튜토리얼)

파일 내에서 문자열을 대체하려면, 튜토리얼 매크로에 아홉번째와 열번째 줄을 추가합니다:

## \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);
n = document.selection.Replace( "editor", "######", eeReplaceAll );
alert( n + " strings found!" );
```

## \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"
n = document.selection.Replace( "editor", "######", eeReplaceAll )
alert n & " strings found!"
```
위의 매크로를 저장하고 새로운 엠에디터 창에 매크로를 실행합니다.
두개의 "editor" 문자열이 대,소문자를 구분하여 검색하여 문자열 "######"로 대체된 후,
"Two strings found!" 텍스트 메시지 박스가 표시된것을 알 수 있습니다.
[Replace 메서드](../selection/selectionreplace) 의 첫번째 인수는
검색할 문자열을 지정하고, 두번째 인수는 대체될 문자열을 지정하며, 세번째 인수는
플래그 결합을 지정합니다. 메서드는 대체된 문자열의 숫자를 반환합니다.
세번째 인수에 eeReplaceAll을 지정한 경우, 메서드는 문자열을 한 번에 대체하고 1보다 많은 수를 반환할 것입니다.
세번째 인수의 플래그에 관한 더 자세한 설명은 [Replace 메서드](../selection/selectionreplace) 의 인수 설명을 참조하십시오.
기본적으로 [Find 메서드](../selection/selectionfind) 와 같이
[Replace 메서드](../selection/selectionreplace) 에서는 검색 문자열이 발견되지 않을 시
매크로 실행이 중단되지 않습니다.
하지만, 예외가 있습니다.
매크로 메뉴 아래임시 옵션으로 실행 명령에서
[매크로 임시 옵션\
대화 상자](../../dlg/macrotempoptions/index) 를 가져와검색 실패시 중지
체크 박스를 선택하고 매크로를 실행하는 경우, 검색 문자열이 발견되지 않을 시 매크로 실행이 중단됩니다.
더 자세한 정보는 튜토리얼의 [파일 내에서 찾기](tutorialfind) 를 참조하십시오.
