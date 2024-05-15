# GetKeyState 方法 (Shell 对象)

检索指定虚拟按键的状态。

## 

### \[JavaScript\]

```
nStatus = shell.GetKeyState( nVirtKey );
```

### \[VBScript\]

```
nStatus = shell.GetKeyState( nVirtKey )
```

## 参数

_nVirtKey_

虚拟键。如果所需的虚拟键是一个字母或数字（A 至 Z，a 至 z，或 0 至 9），则 nVirtKey 必须设置为该字符的 ASCII 值。对于其他键，它必须是一个[虚拟键代码](https://learn.microsoft.com/zh-cn/windows/win32/inputdev/virtual-key-codes)。

## 示例

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

如果键被按下则返回负值。如果低位是 1，则键被切换（例如 CAPS LOCK 键）。

## 版本

支持 EmEditor Professional 24.2 或之后的版本。
