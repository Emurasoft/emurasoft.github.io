# GetKeyState メソッド (Shell オブジェクト)

指定する仮想キーのステータスを取得します。

## 

### \[JavaScript\]

```
nStatus = shell.GetKeyState( nVirtKey );
```

### \[VBScript\]

```
nStatus = shell.GetKeyState( nVirtKey )
```

## パラメータ

_nVirtKey_

仮想キー。指定する仮想キーが文字または数字 (A から Z, a から z, または 0 から 9) の場合、nVirtKey はその文字の ASCII 値になります。その他のキーは、[仮想キー コード](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) になります。

## 例

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

## 戻り値

負の値は、キーが押されていることを示します。最下位ビットが 1 の場合、キーがトグルされています (たとえば、CAPS LOCK キーなど)。

## バージョン

EmEditor Professional Version 24.2 以上で利用できます。
