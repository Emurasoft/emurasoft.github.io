# Saved 屬性 (Document ��H)

檢索或設置表示自從上次被保存或打開后文檔是否已被修改的標志。

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

支持 EmEditor 4.00 或之後的版本。
