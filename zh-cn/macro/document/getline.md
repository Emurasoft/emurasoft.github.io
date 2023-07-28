# GetLine 方法 (Document 对象)

检索指定行上的文本。

## 

### \[JavaScript\]

```
str = document.GetLine( yLine [, nFlags ] );
```

### \[VBScript\]

```
str = document.GetLine( yLine [, nFlags ] )
```

## 参数

_yLine_

指定要检索的文本的行号。

_nFlags_

可选项。你能指定一个下列值的组合。如果你不指定任何值，EmEditor 会默认指定没有返回代码的逻辑坐标。

|     |     |
| --- | --- |
| eeGetLineView | 在视图中指定坐标。 |
| eeGetLineWithNewLines | 添加返回代码到文本中。 |

## 版本

支持 EmEditor 7.00 或之后的版本。
