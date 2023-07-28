# Add 方法 (KeyboardList 集合)

添加一個項目。

## 

### \[JavaScript\]

```
list.Add( nKey, nFlags, nCommand );
```

### \[VBScript\]

```
list.Add nKey, nFlags, nCommand
```

## 參數

_nKey_

指定要添加的項目的按鍵。

_nFlags_

從如下值中指定一個組合。

|     |     |
| --- | --- |
| eeVirtualKey | 指定對象的 Key 成員是一個虛擬鍵代碼。如果這個標志沒有指定，那么對象的 Key 成員被假定為指定一個字元代碼。 |
| eeShift | 指定必須按下 SHIFT 鍵當按下加速鍵時。 |
| eeCtrl | 指定必須按下 CTRL 鍵當按下加速鍵時。 |
| eeAlt | 指定必須按下 ALT 鍵當按下加速鍵時。 |

_nCommand_

指定要添加的項目的命令 ID。

## 版本

支持 EmEditor 7.00 或之後的版本。
