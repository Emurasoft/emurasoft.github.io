# GetKeyState 方法 (Shell 對象)

檢索指定虛擬按鍵的狀態。

## 

### \[JavaScript\]

```
nStatus = shell.GetKeyState( nVirtKey );
```

### \[VBScript\]

```
nStatus = shell.GetKeyState( nVirtKey )
```

## 參數

_nVirtKey_

虛擬按鍵。如果所需的虛擬按鍵是一個字母或數字（A 至 Z，a 至 z，或 0 至 9），則 nVirtKey 必須設定為該字元的 ASCII 值。對於其他鍵，它必須是一個 [Virtual-Key 代碼](https://learn.microsoft.com/zh-tw/windows/win32/inputdev/virtual-key-codes)。

## 範例

### \[JavaScript\]

```
nStatus = shell.GetKeyState( 0x11 );  // CTRL key
if( nStatus < 0 ) {
   alert( "the CTRL key is pressed" );
}
```

### \[VBScript\]

```
nStatus = shell.GetKeyState( &H11 )  // CTRL key
If nStatus < 0 Then
   alert "the CTRL key is pressed"
End If
```

## 返回值

如果鍵被按下則返回負值。如果低位是 1，則鍵被切換（例如 CAPS LOCK 鍵）。

## 版本

支持 EmEditor Professional 24.2 或之後的版本。
