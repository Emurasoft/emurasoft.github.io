# Saved 属性 (Document 对象)

检索或设置表示自从上次被保存或打开后文档是否已被修改的标志。

## 

### \[JavaScript\]

```
bSaved = document.Saved;
document.Saved = bSaved;
```

### \[VBScript\]

```
bSaved = document.Saved
document.Saved = bSaved
```

## 示例

### \[JavaScript\]

```
if( document.Saved )  alert( "The document is not changed." );
else  alert( "The document is changed." );
```

### \[VBScript\]

```
If document.Saved Then
alert( "The document is not changed." )
Else
alert( "The document is changed." )
End If
```

## 版本

支持 EmEditor 4.00 或之后的版本。
