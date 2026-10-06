# FastView 屬性（Document 對象）

獲取或設定文檔是否處於快速檢視模式。

##

### \[JavaScript\]

```javascript
bFastView = document.FastView;
document.FastView = bFastView;
```

### \[VBScript\]

```vbscript
bFastView = document.FastView
document.FastView = bFastView
```

## 備註

將此屬性設定為 **true** 會以快速檢視模式重新打開文檔；將其設定為 **false** 會以普通模式重新打開文檔，效果與 **Fast View** 命令相同。如果文檔已經處於指定模式，則不會發生任何操作。

此屬性只能對活動文檔進行設定。如果文檔無法切換到指定模式（例如文檔尚未命名），則設定此屬性會失敗。

當文檔以快速檢視模式打開時，隨後對該文檔的巨集調用會等待，直到 EmEditor 讀完該文檔。

## 範例

### \[JavaScript\]

```javascript
if( document.FastView )  alert( "The document is in Fast View mode." );
else  alert( "The document is not in Fast View mode." );
document.FastView = true;
```

### \[VBScript\]

```vbscript
If document.FastView Then
alert( "The document is in Fast View mode." )
Else
alert( "The document is not in Fast View mode." )
End If
document.FastView = True
```

## 版本

支持 EmEditor Professional 26.3 或更高版本。