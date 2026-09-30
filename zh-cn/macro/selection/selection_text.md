# Text 属性 (Selection 对象)

获取被选取的文本，或在光标位置处插入一个字符串。如果在检索文本时文本过长，则该属性会失败。在使用 V8 时，支持的最大长度（以 UTF-16 字符计）为 0x19fffffe；否则为 0x3ffffffe。

## 

### \[JavaScript\]

```
str = document.selection.Text;
document.selection.Text = str;
```

### \[VBScript\]

```
str = document.selection.Text
document.selection.Text = str
```

## 示例

### \[JavaScript\]

```
str = document.selection.Text;
alert( "The selected text is " + str );
document.selection.Text = "Hello";
```

### \[VBScript\]

```
str = document.selection.Text
alert "The selected text is " & str
document.selection.Text = "Hello"
```

## 版本

支持 EmEditor 4.00 或之后的版本。
