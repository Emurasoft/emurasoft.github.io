# FastView 属性（Document 对象）

获取或设置文档是否处于快速查看模式。

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

## 备注

将此属性设置为 **true** 会以快速查看模式重新打开文档；将其设置为 **false** 会以普通模式重新打开文档，效果与 **Fast View** 命令相同。如果文档已经处于指定模式，则不会发生任何操作。

此属性只能对活动文档进行设置。如果文档无法切换到指定模式（例如文档尚未命名），则设置此属性会失败。

当文档以快速查看模式打开时，随后对该文档的宏调用会等待，直到 EmEditor 读完该文档。

## 示例

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