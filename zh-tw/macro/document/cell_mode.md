# CellMode 屬性 (Document 對象)

設置或檢索一個標志來顯示選擇模式是否是儲存格選擇模式。

## 

### \[JavaScript\]

```
b = document.CellMode;
document.CellMode = b;
```

### \[VBScript\]

```
b = document.CellMode
document.CellMode = b
```

## 范例

### \[JavaScript\]

```
if( document.CellMode )  alert( "儲存格選擇模式." );
else  alert( "不是儲存格選擇模式." );
```

### \[VBScript\]

```
If document.CellMode Then
alert( "儲存格選擇模式." )
Else
alert( "不是儲存格選擇模式." )
End If
```

## 版本

支持 EmEditor 15.8 或之後的版本。
