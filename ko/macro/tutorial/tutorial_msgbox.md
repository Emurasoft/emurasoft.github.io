# 메시지 상자 표시 (튜토리얼)

간단한 텍스트를 메시지 박스에 표시하려면, [alert 메서드](../window/window_alert)
또는 [confirm 메서드](../window/window_confirm) 를 사용합니다.
하지만, 이 메서드들은 오직 세가지의 버튼만을 나타낼 수 있습니다: YES, NO, 및 CANCEL.
더 복잡한 텍스트를 메시지 박스에 표시하려면 WshShell 개체의 Popup 메서드를 사용합니다.

다음의 예제 코드는 Continue? 텍스트를 표시한 후 YES, NO, 및 CANCEL 버튼을 표시합니다.
변수 n은 YES 버튼이 선택되면 6으로, NO 버튼이 선택된 경우 7로, CANCEL 버튼이 선택된 경우 2로 할당됩니다.

## 

### \[JavaScript\]

```
WshShell = new ActiveXObject( "WScript.Shell" );
n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 );
```

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 )
```

## 참조:
