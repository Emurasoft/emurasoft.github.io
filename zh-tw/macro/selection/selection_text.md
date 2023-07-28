# Text 屬性 (Selection 對象)

檢索被選取的文字，或在游標位置處插入一個字串。

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

支持 EmEditor 4.00 或之後的版本。
