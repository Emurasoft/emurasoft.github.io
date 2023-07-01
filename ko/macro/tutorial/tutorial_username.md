# 컴퓨터 사용자의 이름 얻기 (Ʃ�丮��)

컴퓨터 사용자의 이름을 얻으려면 WshNetwork 개체의 UserName 속성을 사용합니다.

다음의 예제는 현재 컴퓨터 사용자의 이름을 얻는 방법을 보여줍니다:

#### \[JavaScript\]

WshNetwork = new ActiveXObject( "WScript.Network" );

alert( "User Name = " + WshNetwork.UserName );

#### \[VBScript\]

Set WshNetwork = CreateObject( "WScript.Network" )

alert "User Name = " & WshNetwork.UserName

## 참조:

.aspx)
