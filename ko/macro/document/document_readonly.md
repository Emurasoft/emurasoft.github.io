# ReadOnly 속성 (Document 개체)

문서의 읽기 전용 상태를 설정합니다.

## 

### \[JavaScript\]

```
bReadOnly = document.ReadOnly;
document.ReadOnly = bReadOnly;
```

### \[VBScript\]

```
bReadOnly = document.ReadOnly
document.ReadOnly = bReadOnly
```

## 예시

### \[JavaScript\]

```
if( document.ReadOnly )  alert( "The document is read-only" );
else  alert( "The document is not read-only." );
```

### \[VBScript\]

```
If document.ReadOnly Then
alert( "The document is read-only" )
Else
alert( "The document is not read-only." )
End If
```

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
