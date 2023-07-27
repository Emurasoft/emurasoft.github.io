# prompt 方法 (Window ����)

显示一个对话框来输入字符串。

## 

### \[JavaScript\]

```
strAnswer =prompt( strMessage, strDefault, flags);
```

### \[VBScript\]

```
strAnswer =prompt( strMessage, strDefault, flags )
```

## 参数

_strMessage_

指定要显示的消息。

_strDefault_

指定一个默认字符串显示在该文本框中。

_flags_

可选。指定以下值之一。如果省略，则指定为 0。

|     |     |
| --- | --- |
| 0 | 显示单行文本框。 |
| eePromptMultiline | 显示多行文本框。 |

## 返回值

在文本框中返回用户输入的字符串如果选择了「OK」按钮，或者返回一个空字符串如果选择了「Cancel」。

## 版本

支持 EmEditor 4.00 或之后的版本。
