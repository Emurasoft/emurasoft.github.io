# Flags 屬性 (KeyboardItem 對象)

指定對象的標志。

## 

### \[JavaScript\]

```
n = item.Flags;
item.Flags = n;
```

### \[VBScript\]

```
n = item.Flags
item.Flags = n
```

## 參數

_n_

從下列值中選擇。

|     |     |
| --- | --- |
| eeVirtualKey | 指定對象的 Key 成員是一個虛擬鍵代碼。如果這個標志沒有指定，那么對象的 Key 成員被假定為指定一個字元代碼。 |
| eeShift | 指定必須按下 SHIFT 鍵當按下加速鍵時。 |
| eeCtrl | 指定必須按下 CTRL 鍵當按下加速鍵時。 |
| eeAlt | 指定必須按下 ALT 鍵當按下加速鍵時。 |

## 版本

支持 EmEditor 7.00 或之後的版本。
