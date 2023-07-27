# ReadOnly 属性 (Document ����)

检索或设置文档是否为只读。

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

## 示例

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

## 版本

支持 EmEditor 4.00 或之后的版本。
