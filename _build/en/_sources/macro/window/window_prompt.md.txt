# prompt 方法

顯示一個對話方塊來輸入字串。

#### \[JavaScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_);

#### \[VBScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_ )

## 參數

_strMessage_

指定要顯示的消息。

_strDefault_

指定一個預設字串顯示在該文字方塊中。

_flags_

可選。指定以下值之一。如果省略，則指定為 0。

|     |     |
| --- | --- |
| 0 | 顯示單行文字方塊。 |
| eePromptMultiline | 顯示多行文字方塊。 |

## 返回值

在文字方塊中返回使用者輸入的字串如果選擇了「OK」按鈕，或者返回一個空字串如果選擇了「Cancel」。

## 版本

支持 EmEditor 4.00 或之後的版本。