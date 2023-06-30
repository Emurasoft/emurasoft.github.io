# 개체 생성 (Ʃ�丮��)

이 섹션은 Windows에서 사용 가능한 다른 개체들을 사용하는 편리한 방법을 소개합니다.
개체들을 사용하기 위해 JavaScript에서 ActiveXObject 개체를 사용하거나
VBScript에서 CreateObject 기능을 사용합니다.

다음의 예문에서는 현재 디렉토리를 표시하기 위해 WScript.Shell 개체를 사용하였습니다.

#### \[JavaScript\]

WshShell = new ActiveXObject( "WScript.Shell" );

alert( WshShell.CurrentDirectory );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

alert WshShell.CurrentDirectory

## 참조: