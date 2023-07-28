# clearData 方法 (clipboardData 對象)

從剪貼簿上刪除一個或多個數據格式。

## 

### \[JavaScript\]

```
clipboardData.clearData( [ sDataFormat, [ iPos ] ] );
```

### \[VBScript\]

```
clipboardData.clearData [ sDataFormat, [ iPos ] ]
```

## 參數

_sDataFormat_

可選項。指定一個或多個下列數據格式值的字符串。如果省略，所有可用的格式都會被刪除。

|     |     |
| --- | --- |
| Text | 刪除所有格式包括文本。 |
| LineText | 刪除行文本格式。 |
| BoxText | 刪除框文本格式。 |

_iPos_

可選項。在剪貼簿記錄中指定位置如果您想要刪除舊的剪貼簿記錄。如果這個參數是零或被省略，當前的數據會被刪除。

## 示例

### \[JavaScript\]

```
clipboardData.clearData();
```

### \[VBScript\]

```
clipboardData.clearData
```

## 版本

支持 EmEditor 5.00 或之後的版本。
