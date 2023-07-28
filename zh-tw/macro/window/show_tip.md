# ShowTip 方法 (Window 對象)

顯示工具提示。

## 

### \[JavaScript\]

```
ShowTip( strTip, flags );
```

### \[VBScript\]

```
ShowTip strTip, flags
```

## 參數

_strTip_

指定要在工具提示中顯示的文字。文字長度不能超過 3,999 個字元。該字串可包含以這種格式指定的可點擊文字："<a href="url">可點擊文字</a>"。

_flags_

指定下列值之一。

|     |     |
| --- | --- |
| eeShowTipActiveString | 在游標懸停的主動字串處顯示工具提示。 |
| eeShowTipCurrentCaret | 在插入符號位置顯示工具提示。 |
| eeShowTipCurrentMouse | 在游標指針位置顯示工具提示。 |
| eeShowTipHide | 如果已經顯示，隱藏工具提示。 |

## 版本

支持 EmEditor 16.9 或之後的版本。
