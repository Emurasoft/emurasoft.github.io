# GetKeyState Method (Shell Object)

Retrieves the status of the specified virtual key.

## 

### \[JavaScript\]

```
nStatus = shell.GetKeyState( nVirtKey );
```

### \[VBScript\]

```
nStatus = shell.GetKeyState( nVirtKey )
```

## Parameters

_nVirtKey_

A virtual key. If the desired virtual key is a letter or digit (A through Z, a through z, or 0 through 9), nVirtKey must be set to the ASCII value of that character. For other keys, it must be a [virtual-key code](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).

## Examples

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

## Return Value

A negative value if the key is down. If the low-order bit is 1, the key is toggled (such as the CAPS LOCK key).

## Version

Supported on EmEditor Professional Version 24.2 or later.
