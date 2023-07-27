# 레지스트리 조작 (Ʃ�丮��)

레지스트리를 조작하려면, WshShell 개체의 RegRead 메서드, RegWrite 메서드, 및 RegDelete 메서드를 사용합니다.

다음의 예제 코드는 레지스트리로부터 실행되는 매크로의 파일 이름을 읽고, 그것을 표시합니다.

## 

### \[JavaScript\]

```
WshShell = new ActiveXObject( "WScript.Shell" );
str = WshShell.RegRead( "HKCU\\\Software\\\EmSoft\\\EmEditor v3\\\Common\\\MacroFile"
);
alert( str );
```

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
str = WshShell.RegRead( "HKCU\\Software\\EmSoft\\EmEditor v3\\Common\\MacroFile" )
alert str
```

## 팁:

JavaScript에서 문자열 내에 백 슬래시 "\\"를 포함하기 원하는 경우 또다른 하나의 백 슬래시 "\\"가 이전에 배치되어야만 합니다 ("\\\").

## 참조:
